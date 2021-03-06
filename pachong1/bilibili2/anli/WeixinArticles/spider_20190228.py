from urllib.parse import urlencode

import pymongo
from lxml.etree import XMLSyntaxError
from pyquery import PyQuery as pq
import requests
from .config import *


client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


base_url = 'https://weixin.sogou.com/weixin?'

headers = {     #以实际为准，这里只是演示
    'Cookie':'',
    'Host':'weixin.sougou.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':''
}
proxy_pool_url = 'http://127.0.0.1:5000/get'
proxy = None


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def get_html(url,count=1):
    print('Crawling',url)
    print('Trying Count',count)
    global proxy
    if count >=MAX_COUNT:
        print('Tried Too Many Counts')
        return None

    try:
        if proxy:
            proxies = {
                'http':'http://' + proxy
            }
            response = requests.get(url,allow_redirects=False,headers = headers,proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code ==200:
            return response.text
        if response.status_code == 302:
            # Need Proxy
            print('302')
            proxy = get_proxy()
            if proxy:
                print('Using Proxy',proxy)
                return get_html(url)
            else:
                print('Get Proxy Failed')
                return None

    except ConnectionError as e:
        print('Error Occurred',e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url,count)

def get_index(keyword,page):
    data = {
        'query':keyword,
        'type':2,
        'page':page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html
def parse_index(html):
    doc = pq(html)
    items = doc('.new-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')
def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None
def parse_detail(html):
    try:
        doc = pq(html)
        title = doc('.rich_media_title').text()
        content = doc('.rich_media_content').text()
        date = doc('#post-date').text()
        nickname = doc('#js_profile_qrcode > div > strong').text()
        wechat = doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        return {
            'title':title,
            'content':content,
            'date':date,
            'nickname':nickname,
            'wechat':wechat
        }
    except XMLSyntaxError:
        return None
def save_to_mongo(data):
    if db['articles'].update({'title':data['title']},{'$set':data},True):
        print('Saved to Mongo',data['title'])
    else:
        print('Saved to Mongo Failed',data['title'])

def main():
    for page in range(1,100):
        html = get_index(KEYWORD,page)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                article_html = get_detail(article_url)
                if article_html:
                    article_data = parse_detail(article_html)
                    if article_data:
                        save_to_mongo(article_data)



if __name__ == '__main__':
    main()