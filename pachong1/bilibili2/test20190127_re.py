import re

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$',content)
print(result)
print(result.group())
print(result.span())

# 匹配目标
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld.*Demo$',content)
print(result)
print(result.group(1))
print(result.span())
# 贪婪模式
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+)\sWorld.*Demo$',content)
print(result)
print(result.group(1))
# 非贪婪模式
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+)\sWorld.*Demo$',content)
print(result)
print('0:',result.group(1))
# 匹配模式，换行符
content = '''Hello 1234567 World_This 
is a Regex Demo
'''
# result = re.match('^He.*?(\d+).*?Demo$',content)
# print('1:',result)
result = re.match('^He.*?(\d+).*?Demo$',content,re.S)
print('2:',result.group(1))
# 转译
content='price is $5.00'
result = re.match('price is \$5\.00',content)
print('3:',result)

# re.search
# re.search 扫描整个字符串并返回第一个成功的匹配
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result=re.search('Hello.*?(\d+).*?Demo',content)
print('4:',result)
print('4.2:',result.group(1))

# re,findall
html=''
results=re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print('5:',results)
print(type(results))
for result in results:
    print(result)
    print(result[0],result[1],result[2])

# re.sub
# 替换字符串中每一个匹配的子串后返回替换后的字符串
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
content = re.sub('\d+','',content)
print('6:',content)
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
content = re.sub('(\d+)',r'\1 8910',content)
print('7:',content)

html=''
html = re.sub('<a.*?>|</a>','',html)    #去掉网页中的a标签
results=re.findall('<li.*?>(.*>?)</li>',html,re.S)
print(results)
for result in results:
    print(result.strip())   #strip() 方法是去掉换行符


# re.compile
# 将正则字符串编译成正则表达式对象,主要是代码复用
content = 'Hello 123 4567 World_This is a Regex Demo'
pattern = re.compile('^Hello.*Demo$',re.S)
result = re.match(pattern,content)
print(result)