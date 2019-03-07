import pandas
import os
import pyecharts
from pyecharts import Bar
import numpy

data = pandas.read_excel('e:/房价与工资.xlsx')
print(data,data.shape)
x=numpy.arange(0,11)
y1=data["房屋均价"].values
y2=data["平均工资"].values
print(x,y1,y2)
bar = Bar()
bar.add("房屋均价",x,y1,mark_point=["max","min"],mark_line=["average"],is_label_show=True)
bar.add("人均工资",x,y2)
bar.render("bar.html")
