import numpy
from numpy import genfromtxt
from matplotlib import pyplot

# 载入数据
data = numpy.genfromtxt("data.csv",delimiter=",")
x_data = data[:,0,numpy.newaxis]
y_data = data[:,1,numpy.newaxis]
pyplot.scatter(x_data,y_data)
pyplot.show()


print(numpy.mat(x_data).shape)
print(numpy.mat(y_data).shape)
# 给样本添加偏置项
X_data = numpy.concatenate((numpy.ones((100,1)),x_data),axis=1)
print(X_data.shape)
print(X_data[:3])


# 标准方程法求解回归参数
def weights(xArr,yArr):
    xMat = numpy.mat(xArr)
    yMat = numpy.mat(yArr)
    xTx = xMat.T*xMat   #矩阵乘法
#     计算矩阵的值，如果是0，说明该矩阵没有逆矩阵
    if numpy.linalg.det(xTx) ==0.0:
        print("This matrix cannot do inverse")
        return
#     xTx.I为xTx的逆矩阵
    ws = xTx.I*xMat.T*yMat
    return ws


ws = weights(X_data,y_data)
print(ws)


# 画图
x_test = numpy.array([[20],[80]])
y_test = ws[0] ++ x_test*ws[1]
pyplot.plot(x_data,y_data,'b.')
pyplot.plot(x_test,y_test,'r')
pyplot.show()


