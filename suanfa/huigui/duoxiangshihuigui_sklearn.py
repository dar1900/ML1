import numpy
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot
from sklearn.preprocessing import PolynomialFeatures


# 载入数据
data=numpy.genfromtxt("job.csv",delimiter=",")
x_data = data[1:,1]
y_data = data[1:,2]
pyplot.scatter(x_data,y_data)
pyplot.show()
# print(x_data,y_data)


# x_data = data[1:,1,numpy.newaxis]
# y_data = data[1:,2,numpy.newaxis]
x_data = x_data[:,numpy.newaxis]
y_data = y_data[:,numpy.newaxis]
# 创建并拟合模型
model = LinearRegression()
model.fit(x_data,y_data)


# 画图
pyplot.plot(x_data,y_data,'b')
pyplot.plot(x_data,model.predict(x_data),'r')
pyplot.show()


# 定义多项式回归，degree的值可以调节多项式的特征
#1是一次方，2是二次方，3是三次方,也可以设置为5，是多项式的最高次项
poly_reg = PolynomialFeatures(degree=3)
# 特征处理
x_ploy = poly_reg.fit_transform(x_data)
# 定义回归模型
lin_reg = LinearRegression()
# 训练模型
lin_reg.fit(x_ploy,y_data)
print(x_ploy)


# 画图
pyplot.plot(x_data,y_data,'b.')
pyplot.plot(x_data,lin_reg.predict(poly_reg.fit_transform(x_data)),c='r')
pyplot.title('Truth or Bluff (Polynomial Regression)')
pyplot.xlabel('Position level')
pyplot.ylabel('Salary')
pyplot.show()


