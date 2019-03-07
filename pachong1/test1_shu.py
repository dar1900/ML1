# _*_ coding:utf-8 _*_
import urllib.request
from lxml import html
from bs4 import BeautifulSoup
import time

num=1
start_time=time.time()
url='https://read.douban.com/columns/category/all?sort=hot&start='

for i in range(0,1650,10):
    html=urllib.request.urlopen('https://read.douban.com/columns/category/all?sort=hot&start=%d' % i)
    bsObj=BeautifulSoup(html,'lxml')
    print('==============' + '第%d页'%(i/10 + 1) + '==============')
    h4_node_list=bsObj.find_all('h4')
    for h4_node in h4_node_list:
        a_node =h4_node.contents[0]
        title=a_node.contents[0]
        title='《'+title+'》'
        print('第%d本书'%num, title)
        num=num+1
    time.sleep(1)

end_time=time.time()
duration_time=end_time-start_time
print('运行时间共：%.2f'  % duration_time + '秒')
print('共抓到%d本书名'%num)