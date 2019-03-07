# _*_ coding:utf-8 _*_
import urllib.request
import re
from lxml import html
from bs4 import BeautifulSoup
import time

url='https://www.jianke.com/help/sitemap.html'

html=urllib.request.urlopen(url)
bs=BeautifulSoup(html,'lxml')
a=bs.select('a')
print(a)
# div=bs.find("div",{"class":"map_com"}).find_next('div')
href_list=[]
for k in bs.find_all('a'):
    # print(k['href'],k.string)
    t3=k.get('href')

    href_list.append(t3)
# print(href_list)
# def abc(tag):
#     return  tag.get('href').startwith('http')
# for tag in filter(abc,a):
#     print(tag)
# tag.get('href').startwith('http') and len(tag.get('string'))<10
# def hasHttpLink(tag):
#     """此时的tag为<li>标签，需要取得其中的<a>再来进行判断"""
#     return tag.a is not None and tag.a.get('href').startswith("http")
# for tag in filter(hasHttpLink, bs):
#     print(tag)


# p=r'<a href="*">.+?<a>'
# pattern1=re.compile(p)
# w=pattern1.findall(bs)
# print(w)
# for  i in div.findAll("a"):
#     print(i.a.attrs['href'])