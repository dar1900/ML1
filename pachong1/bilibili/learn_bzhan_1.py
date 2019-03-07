import requests


# url='www.baidu.com'
# r=requests.get(url)


# request库的post（）方法
# 想url post一个字典自动编码为form（表单）
payload = {'key1':'value1','key2':'value2'}
r = requests.post('http://httpbin.org/post',data = payload)
print(r.text)

# 爬取网页的通用代码框架
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()    #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
if __name__=="__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))


# 爬取图片全代码
import requests
import os

url="https://tiem.jd.com/2967929.html"
root="d://pics//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")


# ip地址查询的全代码
import requests
url="https://tiem.jd.com/2967929.html"
try:
    r = requests.get(url+'202.204.80.112')
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")