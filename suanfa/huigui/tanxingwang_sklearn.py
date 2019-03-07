import numpy
from matplotlib import pyplot
from numpy import genfromtxt
from sklearn import linear_model



# 读取数据
data = genfromtxt(r"longley.csv",delimiter=',')
print(data)


# 切分数据
x_data = data[1:,2:]
y_data = data[1:,1]
print(x_data)
print(y_data)


# 创建模型
model = linear_model.ElasticNetCV()
model.fit(x_data,y_data)
# 弹性网系数
print(model.alpha_)
# 相关系数
print(model.coef_)


# 预测
print(model.predict(x_data[-2,numpy.newaxis]))



