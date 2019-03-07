import numpy
from matplotlib import pyplot
from numpy import genfromtxt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model, preprocessing
from sklearn.metrics import classification_report
from sklearn.datasets import make_gaussian_quantiles

# 生成2维正态分布，生成的数据按分位数分为两类，500个样本，2个样本特征
# 可以生成两类或多类数据
x_data, y_data = make_gaussian_quantiles(n_samples=500, n_features=2, n_classes=2)
pyplot.scatter(x_data[:, 0], x_data[:, 1], c=y_data)
pyplot.show()


logistic = linear_model.LogisticRegression()
logistic.fit(x_data, y_data)

# 获取数据值所在的范围
x_min, x_max = x_data[:, 0].min() - 1, x_data[:, 0].max() + 1
y_min, y_max = x_data[:, 1].min() - 1, x_data[:, 1].max() + 1
# 生成网格矩阵
xx, yy = numpy.meshgrid(numpy.arange(x_min, x_max, 0.02),
                        numpy.arange(y_min, y_max, 0.02))
z = logistic.predict(numpy.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)
# 等高线图
cs = pyplot.contourf(xx, yy, z)
# 样本散点图
pyplot.scatter(x_data[:, 0], x_data[:, 1], c=y_data)
pyplot.show()
print('score:', logistic.score(x_data, y_data))


# 定义多项式回归，degree的值可以调节多项式的特征
poly_reg = PolynomialFeatures(degree=5)
# 特征处理
x_poly = poly_reg.fit_transform(x_data)
# 定义逻辑回归模型
logistic = linear_model.LogisticRegression()
# 训练模型
logistic.fit(x_poly, y_data)
# 获取数值所在的范围
x_min, x_max = x_data[:, 0].min() - 1, x_data[:, 0].max() + 1
y_min, y_max = x_data[:, 1].min() - 1, x_data[:, 1].max() + 1
# 生成网格矩阵
xx, yy = numpy.meshgrid(numpy.arange(x_min, x_max, 0.02),
                        numpy.arange(y_min, y_max, 0.02))
z = logistic.predict(poly_reg.fit_transform(numpy.c_[xx.ravel(), yy.ravel()]))
z = z.reshape(xx.shape)
# 等高线图
cs = pyplot.contourf(xx, yy, z)
# 样本散点图
pyplot.scatter(x_data[:, 0], x_data[:, 1], c=y_data)
pyplot.show()
print('score:', logistic.score(x_poly, y_data))
