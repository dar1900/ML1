import json
from _md5 import md5
from json import JSONDecodeError
from multiprocessing.pool import Pool
from urllib.parse import urlencode
import re

import os
import pymongo
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import requests
from pachong1.bilibili2.anli.ajax.config import *

# 2_爬取今日头条图片，处理ajax请求

client = pymongo.MongoClient(MONGO_URL,connect=False)
db = client[MONGO_DB]

# https://www.toutiao.com/api/search/content/?aid=24&offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis
def get_page_index(offset,keyword):
    data = {
        'aid': '24',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from' : 'search_tab',
        'pd' : 'synthesis'
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None
def parse_page_index(html):
    try:
        data = json.loads(html)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except JSONDecodeError:
        pass

def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错',url)
        return None
def parse_page_detail(html,url):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('var gallery = (.*?);',re.S)
    result = re.search(images_pattern,html)
    if result:
        data = json.loads(result.group(1))
        if data and 'sub_images'in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images:download_image(image)
            return {
                'title':title,
                'url':url,
                'images':images
            }
def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储到MongoDB成功',result)
        return True
    return False

def download_image(url):
    print('正在下载',url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)    #返回content是返回二进制请求，网页返回text
        return None
    except RequestException:
        print('请求图片出错',url)
        return None
def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(),md5(content),'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close()


def main(offset):
    html = get_page_index(offset,KEYWORD)
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html,url)
            if result:
                save_to_mongo(result)

if __name__ == '__main__':
    # main()
    grops = [x*20 for x in range(GROUP_START,GROUP_END)]
    pool = Pool()
    pool.map(main,grops)
