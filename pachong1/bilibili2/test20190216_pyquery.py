from pyquery import PyQuery


# 字符串初始化
html=''
doc = PyQuery(html)
print(doc('li'))
#URL 初始化
doc = PyQuery(url='www.baidu.com')
print(doc('head'))
# 文件初始化
doc = PyQuery(filename='deml.html')
print(doc('li'))

# 基本css选择器
doc = PyQuery(html)
print(doc('#container .list li'))

# 超找元素
doc = PyQuery(html)
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)
'''或者'''
lis = items.children()
print(type(lis))
print(lis)
'''或者'''
lis = items.children('.active')
print(lis)
# 父元素
doc = PyQuery(html)
items = doc('.list')
container = items.parent()
print(type(container))
print(container)
'''或者'''
doc = PyQuery(html)
items = doc('.list')
parents = items.parents()
print(type(parents))
print(parents)
'''或者'''
parent = items.parents('.warp')
print(parent)

# 兄弟元素
doc = PyQuery(html)
li = doc('.list .item-0.active')
print(li.siblings())
print(li.siblings('.active'))

# 遍历
# 单个元素
doc = PyQuery(html)
li = doc('.item-0.active')
print(li)
# 多个元素
doc = PyQuery(html)
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li)


# 获取信息
# 获取属性
doc = PyQuery(html)
a = doc('.item-0.active a')
print(a)
print(a.attr('href'))
print(a.attr.href)
# 获取文本
print(a.text())
# 获取HTML
print(a.html())


# DOM操作
'''addClass removeClass'''
doc = PyQuery(html)
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)
# attr css
doc = PyQuery(html)
li = doc('.item-0.active')
print(li)
li.attr('name','link')
print(li)
li.css('font-size','14px')
print(li)
# remove
doc = PyQuery(html)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())


# 伪类选择器
doc = PyQuery(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')    #获取2以后得标签
print(li)
li = doc('li:nth-child(2n)')    #获取偶数标签
print(li)
li = doc('li:contains(second)')
print(li)