import numpy
from matplotlib import pyplot

# 载入数据
data = numpy.genfromtxt("../data/data.csv", delimiter=",")
x_data = data[:, 0, numpy.newaxis]
y_data = data[:, 1, numpy.newaxis]
pyplot.scatter(x_data, y_data)
pyplot.show()
print(x_data.shape)


# 数据中心话
def zeroMean(dataMat):
    # 按列求平均值，即各个特征的平均值
    meanVal = numpy.mean(dataMat, axis=0)
    newData = dataMat - meanVal
    return newData, meanVal
newData, meanVal = zeroMean(data)
# numpy.cov 用于求协方差矩阵，
# 参数rowvar=False说明数据一行代表一个样本
# True，即为默认值，表示数据每一列代表一个样本
covMat = numpy.cov(newData, rowvar=False)
print(covMat)  # 协方差矩阵
# numpy.linalg.eig求矩阵的特征值和特征向量
eigVals, eigVects = numpy.linalg.eig(numpy.mat(covMat))
# 特征值
print(eigVals)
# 特征向量
print('eigVects:',eigVects)
# 对特征值从小打到大排序
eigValIndice = numpy.argsort(eigVals)
print('eigValIndice:',eigValIndice,eigValIndice.dtype)
top = 1
# 最大的top个特征值的下标
n_eigValIndice = eigValIndice[-1: -(top + 1):-1]  # 最后 :-1 表示从右往左取数，不加表示从左往右取数
print('n_eigValIndice:', n_eigValIndice)
# 最大的n个特征值对应的特征向量
n_eigVect = eigVects[:, n_eigValIndice]
print(n_eigVect)
# 低维特征空间的数据
lowDDataMat = newData * n_eigVect
print(lowDDataMat)
# 利用低维度数据来重构数据
reconMat = (lowDDataMat*n_eigVect.T)+meanVal
print('reconMat:',reconMat)


# 载入数据
data = numpy.genfromtxt("../data/data.csv", delimiter=",")
x_data = data[:, 0, numpy.newaxis]
y_data = data[:, 1, numpy.newaxis]
pyplot.scatter(x_data, y_data)
# 重构的数据
x_data=numpy.array(reconMat)[:,0]
y_data=numpy.array(reconMat)[:,1]
pyplot.scatter(x_data,y_data,c='r')
pyplot.show()