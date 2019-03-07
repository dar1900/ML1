import requests
url="https://tiem.jd.com/2967929.html"
kv={'user-agent':'Mozilla/5.0'}
try:
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print("连接失败")

# 笔记1
kv = {'wd':'python'}
r=requests.get(url,params=kv)   #提交搜索引擎的搜索内容
# 笔记1,爬取图片
import requests
path = "d:/abc.jpg"
url="https://tiem.jd.com/2967929.html"
r=requests.get(url)
r.status_code
with open(path,'wb') as f:
    f.write(r.content)
    f.close()
    # r.conten 是二进制，写入到文件中

# 笔记2


