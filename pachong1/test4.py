# _*_ coding:utf-8 _*_
import urllib.request
import re
from lxml import html
from bs4 import BeautifulSoup
import time


url='https://search.jianke.com/list-010301.html'
html=urllib.request.urlopen(url)
bs=BeautifulSoup(html,'lxml')
# print(bs)
href_list=[]
name=bs.select('.pro-botxt p a')
nameDict={}
for n in name:
    print(n.get_text())

# def abc(tag):
#     return tag.a is not None and tag.a.get('')


# for k in bs.find_all('a'):
#     print(k.string)
    # t3=k.get('string')
    # href_list.append(t3)
# print(href_list)