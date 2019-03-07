import numpy
from matplotlib import pyplot
from numpy import genfromtxt
from sklearn import linear_model

# 读取数据
data = genfromtxt(r"longley.csv", delimiter=',')
print(data)

# 切分数据
x_data = data[1:, 2:]
y_data = data[1:, 1, numpy.newaxis]
print(x_data)
print(y_data)

print(numpy.mat(x_data).shape)
print(numpy.mat(y_data).shape)
# 给样本添加偏置项
X_data = numpy.concatenate((numpy.ones((16, 1)), x_data), axis=1)
print(X_data)
print(X_data[:3])


# 岭回归标准方程法来求解回归参数
def weights(xArr, yArr, lam=0.2):
    xMat = numpy.mat(xArr)
    yMat = numpy.mat(yArr)
    xTx = xMat.T * xMat  # 矩阵乘法
    rxTx = xTx + numpy.eye(xMat.shape[1]) * lam
    #     计算矩阵的值，如果是0，说明该矩阵没有逆矩阵
    if numpy.linalg.det(rxTx) == 0.0:
        print("This matrix cannot do inverse")
        return
    #    xTx.I为xTx的逆矩阵
    ws = rxTx.I * xMat.T * yMat
    return ws


ws = weights(X_data, y_data)
print(ws)

# 计算预测值
print(numpy.mat(X_data) * numpy.mat(ws))
