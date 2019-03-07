from bs4 import BeautifulSoup

html=''
soup =BeautifulSoup(html,'lxml')
print(soup.prettify())  #prettify() 格式化网页源代码
print(soup.title.string)    #显示title标签内容
print(soup.title)   #显示title标签,带<title></title>
print(type(soup.title))      #显示title标签类型,Tag类型
print(soup.head)    #显示head标签及其内容
print(soup.p)   #显示p标签及其内容，只显示第一个；如果有多个只返回第一个

# 获取名称
print(soup.title.name)  #最外层标签的名称
# 获取属性,二选一
print(soup.p.attrs['name'])
print(soup.p['name'])
# 获取内容
print(soup.p.string)
# 嵌套选择
print(soup.head.title.string)
# 子节点和子孙节点
print(soup.p.contents)  #子节点的元素都会显示出来，列表的形式
# 或者
print(soup.p.children)  #迭代器，需要用循环的方式才能取到内容
for i,child in enumerate(soup.p.children):
    print(i,child)
# 子孙节点:
print(soup.p.descendants)
for i,child in enumerate(soup.p.descendants):
    print(i,child)

# 父节点和祖先节点
print(soup.a.parent)
print(list(enumerate(soup.a.parents)))  #祖先节点
# 兄弟节点
print(list(enumerate(soup.a.next_siblings)))    #后面的兄弟节点
print(list(enumerate(soup.a.previous_siblings)))    #前面的兄弟节点

# 标准选择器
'''
find_all(name,attrs,reursive,text,**kwargs)
可根据标签名、属性、内容查找文档
'''
# name
print(soup.find_all('ul'))
print(type(soup.find_all('ul')[0]))
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))
# attrs
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))
'''或者'''
print(soup.find_all(id='list-1'))
print(soup.find_all(name='elements'))
# text
print(soup.find_all(text='Foo'))    #返回的是标签的内容
'''
find(name,attrs,reursive,text,**kwargs)
返回单个返回值，用法与find_all类似
'''
'''
 css选择器
 通过select（）直接传入css选择器即可完成选择
'''
print(soup.select('.panel .penal-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))
# 获取属性
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
# 获取内容
for li in soup.select('li'):
    print(li.get_text())