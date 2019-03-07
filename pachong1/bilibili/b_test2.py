# 显示标签tag元素
tag.attrs
tag.attrs['class']
tag.attrs['href']

tag.a.string
type(tag.a.string)

soup.head
soup.head.contents
soup.body.contents
len(soup.body.contents)
soup.body.contents[1]

soup.html.parent

soup.a.next_sibling
soup.a.next_sibling.next_sibling
soup.a.previous_sibling
# 为标签增加换行符，更好显示
print(soup.prettify())

# 提取信息
from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,'html.parse')
soup.find_all('a')
soup.find_all(['a','b'])
for tag in soup.find_all(True):
    print(tag.name)
import re
for tag in soup.find_all(re.compile('b')):  #正则表达式，以b开头的标签
    print(tag.name)
soup.find_all('p','course')
soup.find_all(id='link1')
import re
soup.find_all(id=re.compile('link'))
soup.find_all('a',recursive=False)
soup.find_all(string="Basic Python")
soup.find_all(string=re.compile("Python"))


# 正则表达式
^[A-Za-z]+$     #由26个字母组成的字符串
^[A-Za-z0-9]+$      #由26个字母和数字组成的字符串
^-?\d+$         #整数形式的字符串
^[0-9]*[1-9][0-9]*$     #正整数形式的字符串
[1-9]\d{5}      #中国境内邮政编码，6位
\d{3}-\d{8}|\d{4}-\d{7}     #国内电话号码，010-68913536

# 正则表达式举例1
import re
match = re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0))
#     举例2
import re
match = re.match(r'[1-9]\d{5}','100081 BIT')
if match:
    print(match.group(0))
# 举例3
import re
ls = re.findall(r'[1-9]\d{5}','BIT100081 TSU100084')
ls
# li4
re.split(r'[1-9]\d{5}','BIT100081 TSU100084')
re.split(r'[1-9]\d{5}','BIT100081 TSU100084',maxsplit=1)
# li5
for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU100084'):
    if m:
        print(m.group(0))
# li6
re.sub(r'[1-9]\d{5}','zipcode','BIT100081 TSU100084')
# li7
m = re.search(r'[1-9]\d{5}','BIT100081 TSU100084')
m.string
m.re
m.pos
m.endpos
m.group(0)
m.start()
m.end()
m.span()

result=re.match('^hello\s\d\d\d\d\d{4}\s\w{10}.*Demo$',content)