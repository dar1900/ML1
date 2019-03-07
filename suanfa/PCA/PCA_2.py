# 手写数字识别降为可视化
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
import numpy
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

# 载入数据
digits =load_digits()
# 数据
x_data = digits.data
# 标签
y_data = digits.target
# 分割数据1/4为测试数据，3/4为训练数据
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data)
mlp = MLPClassifier(hidden_layer_sizes=(100,50),max_iter=500)
mlp.fit(x_train,y_train)

# 数据中心话
def zeroMean(dataMat):
    # 按列求平均值，即各个特征的平均值
    meanVal = numpy.mean(dataMat, axis=0)
    newData = dataMat - meanVal
    return newData, meanVal
def pca(dataMat,top):
    newData, meanVal = zeroMean(dataMat)
    # numpy.cov 用于求协方差矩阵，
    # 参数rowvar=False说明数据一行代表一个样本
    # True，即为默认值，表示数据每一列代表一个样本
    covMat = numpy.cov(newData, rowvar=False)
    # numpy.linalg.eig求矩阵的特征值和特征向量
    eigVals, eigVects = numpy.linalg.eig(numpy.mat(covMat))
    # 对特征值从小打到大排序
    eigValIndice = numpy.argsort(eigVals)
    # 最大的top个特征值的下标
    n_eigValIndice = eigValIndice[-1: -(top + 1):-1]  # 最后 :-1 表示从右往左取数，不加表示从左往右取数
    # 最大的n个特征值对应的特征向量
    n_eigVect = eigVects[:, n_eigValIndice]
    # 低维特征空间的数据
    lowDDataMat = newData * n_eigVect
    # 利用低维度数据来重构数据
    reconMat = (lowDDataMat * n_eigVect.T) + meanVal
    # 返回低维特征空间的数据和重构的矩阵
    return lowDDataMat,reconMat
lowDDataMat,reconMat = pca(x_data,2)
# 重构的数据
x=numpy.array(lowDDataMat)[:,0]
y=numpy.array(lowDDataMat)[:,1]
pyplot.scatter(x,y,c='r')
pyplot.show()

predictions = mlp.predict(x_data)
# 重构的数据
x=numpy.array(lowDDataMat)[:,0]
y=numpy.array(lowDDataMat)[:,1]
pyplot.scatter(x,y,c=predictions)
# pyplot.scatter(x,y,c=y_data)
pyplot.show()


lowDDataMat,reconMat=pca(x_data,3)
x=numpy.array(lowDDataMat)[:,0]
y=numpy.array(lowDDataMat)[:,1]
z=numpy.array(lowDDataMat)[:,2]
ax=pyplot.figure().add_subplot(111,projection='3d')
ax.scatter(x,y,z,c=predictions,s=10)    #点为红色
pyplot.show()