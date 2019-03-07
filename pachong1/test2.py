# _*_ coding:utf-8 _*_
import queue
import urllib.request
import re
import fileop
from lxml import html
from bs4 import BeautifulSoup
import time


for k1 in range(0,50):
    tempurlpag="http://www.dianping.com/shanghai/hotel/p%d" %(k1+1)
    op=open(tempurlpag)
    if 'html' not in op.getheader('Content-Type'):
        continue
    data1=op.read().decode(encoding='UTF-8')
    linkre = re.complie(r'onclick="window.open\(\'(.*?)\'\)',re.DOTALL).findall(data1)
    for k2 in range(0,len(linkre)):
        tempurlhotel = "http://www.dianping.com"+linkre[k2]
        queue.append(tempurlhotel)
        fileop.write(tempurlhotel+'\n')
    print('第:  %d  页抓取完成！'%k1)

username = re.compile(r'<img title="(.*?)" alt=',re.DOTALL).findall(data)
print('username',username)


mink = min(int(len(userid)),int(len(reta_total)),int(len(rate_room)))
print('mink',mink)


fileop=open(fileOut,'a',encoding='utf-8')
for k in range(0,mink):
    fileop.write('%12s\t%12s\t%20s\t%15s\t%15s\t%15s\t%15s\t\n' % (hotelid, userid[k], username[k], rate_room[k], rate_service[k], rate_total[k], rate_time[k]))
    fileop.close()

except:
    file_except = open('D:/exception.txt','a')
    file_except.write(tempurl+'\n')
    breaknumber = breaknumber+1