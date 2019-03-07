import numpy
from matplotlib import pyplot
from numpy import genfromtxt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model, preprocessing
from sklearn.metrics import classification_report

# 数据是否标准化
scale = False

# 读取数据
data = genfromtxt("LR-testSet2.txt", delimiter=",")
x_data = data[:, :-1]
y_data = data[:, -1, numpy.newaxis]


def plot():
    x0 = []
    x1 = []
    y0 = []
    y1 = []
    # 切分不同类别的数据
    for i in range(len(x_data)):
        if y_data[i] == 0:
            x0.append(x_data[i, 0])
            y0.append(x_data[i, 1])
        else:
            x1.append(x_data[i, 0])
            y1.append(x_data[i, 1])
    # 画图
    scatter0 = pyplot.scatter(x0, y0, c='b', marker='o')
    scatter1 = pyplot.scatter(x1, y1, c='r', marker='x')
    # 画图例
    pyplot.legend(handles=[scatter0, scatter1], labels=['label0', 'label1'], loc='best')
plot()
pyplot.show()

# 定义多项式回归，degree的值可以调节多项式的特征
poly_reg = PolynomialFeatures(degree=3)
# 特征处理
x_poly = poly_reg.fit_transform(x_data)


def sigmoid(x):
    return 1.0 / (1 + numpy.exp(-x))
def cost(xMat, yMat, ws):
    left = numpy.multiply(yMat, numpy.log(sigmoid(xMat * ws)))
    right = numpy.multiply(1 - yMat, numpy.log(1 - sigmoid(xMat * ws)))
    # multiply是矩阵按位相乘，不是矩阵乘法
    return numpy.sum(left + right) / -(len(xMat))
def gradAscent(xArr, yArr):
    if scale == True:
        xArr = preprocessing.scale(xArr)
    xMat = numpy.mat(xArr)
    yMat = numpy.mat(yArr)
    lr = 0.03
    epochs = 50000
    costList = []
    #     计算数据行列数
    # 行代表数据个数，列代表权值个数
    m, n = numpy.shape(xMat)
    #     初始化权值
    ws = numpy.mat(numpy.ones((n, 1)))
    for i in range(epochs + 1):
        #         xMat和weights矩阵相乘
        h = sigmoid(xMat * ws)
        #         计算误差
        ws_grad = xMat.T * (h - yMat) / m
        ws = ws - lr * ws_grad
        if i % 50 == 0:
            costList.append(cost(xMat, yMat, ws))
    return ws, costList


# 训练模型，得到权值和cost值的变化
ws, costList = gradAscent(x_poly, y_data)
print("ws:", ws)


# 画图
# 获取数据值所在的范围
x_min,x_max = x_data[:,0].min()-1,x_data[:,0].max()+1
y_min,y_max = x_data[:,1].min()-1,x_data[:,1].max()+1
# 生成网络矩阵
# numpy.r_按row来组合array
# numpy.c_按column来组合arra
# a=numpy.array([1,2,3])
# b=numpy.array([5,2,5])
# numpy.r_[a,b]
# arrary=([[1,5],
#          [2,2],
#          [3,5]])
# numpy.c_[a,[0,0,0],b]
# arrary([[1,0,5],
#         [2,0,2],
#         [3,0,5]])
xx,yy=numpy.meshgrid(numpy.arange(x_min,x_max,0.02),numpy.arange(y_min,y_max,0.02))
z=sigmoid(poly_reg.fit_transform(numpy.c_[xx.ravel(),yy.ravel()]).dot(numpy.array(ws)))
# ravel与flatten类似，多维数据转一维，flatten不会改变原始数据,ravel会改变原始数据
for i in range(len(z)):
    if z[i]>0.5:
        z[i]=1
    else:
        z[i]=0
z=z.reshape(xx.shape)
# 等高线图
cs= pyplot.contourf(xx,yy,z)
plot()
pyplot.show()


# 预测
def predict(x_data,ws):
    # if scale ==True:
    #     x_data=preprocessing.scale(x_data)
    xMat = numpy.mat(x_data)
    ws = numpy.mat(ws)
    return [1 if x>0.5 else 0 for x in sigmoid(xMat*ws)]
predictions = predict(x_poly,ws)
print(classification_report(y_data,predictions))

