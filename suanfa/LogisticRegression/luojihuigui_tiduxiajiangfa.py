import numpy
from matplotlib import pyplot
from numpy import genfromtxt
from sklearn import preprocessing
from sklearn.metrics import classification_report
# 数据是否标准化
scale = False
# 如果做了标准化，得到的结果更优化


# 读取数据
data = genfromtxt("LR-testSet.csv",delimiter=",")
x_data = data[:,:-1]
y_data = data[:,-1]
def plot():
    x0=[]
    x1 = []
    y0 = []
    y1 = []
    # 切分不同类别的数据
    for i in range(len(x_data)):
        if y_data[i]==0:
            x0.append(x_data[i,0])
            y0.append(x_data[i,1])
        else:
            x1.append(x_data[i,0])
            y1.append(x_data[i,1])
    # 画图
    scatter0 = pyplot.scatter(x0,y0,c='b',marker='o')
    scatter1 = pyplot.scatter(x1,y1,c='r',marker='x')
    # 画图例
    pyplot.legend(handles=[scatter0,scatter1],labels=['label0','label1'],loc='best')
plot()
pyplot.show()


# 数据处理，添加偏置项
x_data = data[:,:-1]
y_data = data[:,-1,numpy.newaxis]
print("numpy.mat(x_data).shape:",numpy.mat(x_data).shape)
print("numpy.mat(y_data).shape:",numpy.mat(y_data).shape)
# 给样本添加偏置项
X_data = numpy.concatenate((numpy.ones((100,1)),x_data),axis=1)
print("X_data.shape:",X_data.shape)


def sigmoid(x):
    return 1.0/(1+numpy.exp(-x))
def cost(xMat,yMat,ws):
    left = numpy.multiply(yMat,numpy.log(sigmoid(xMat*ws)))
    right = numpy.multiply(1-yMat,numpy.log(1-sigmoid(xMat*ws)))
    # multiply是矩阵按位相乘，不是矩阵乘法
    return numpy.sum(left+right)/-(len(xMat))
def gradAscent(xArr,yArr):
    if scale == True:
        xArr=preprocessing.scale(xArr)
    xMat = numpy.mat(xArr)
    yMat = numpy.mat(yArr)

    lr=0.001
    epochs=10000
    costList=[]
#     计算数据行列数
# 行代表数据个数，列代表权值个数
    m,n = numpy.shape(xMat)
#     初始化权值
    ws = numpy.mat(numpy.ones((n,1)))
    for i in range(epochs+1):
#         xMat和weights矩阵相乘
        h=sigmoid(xMat*ws)
#         计算误差
        ws_grad = xMat.T*(h-yMat)/m
        ws = ws - lr*ws_grad
        if i % 50 ==0:
            costList.append(cost(xMat,yMat,ws))
    return ws,costList

# 训练模型，得到权值和cost值的变化
ws,costList = gradAscent(X_data,y_data)
print("ws:",ws)


# 如果做了数据标准化就不画图，不做可以画图
if scale == False:
#     画图决策边界
    plot()
    x_test = [[-4],[3]]
    y_test = (-ws[0]-x_test*ws[1])/ws[2]
    pyplot.plot(x_test,y_test,'k')
    pyplot.show()


# 画图loss值得变化
x = numpy.linspace(0,10000,201)
pyplot.plot(x,costList,c='r')
pyplot.title('Train')
pyplot.xlabel('Epochs')
pyplot.ylabel('Cost')
pyplot.show()


# 预测
def predict(x_data,ws):
    if scale == True:
        x_data = preprocessing.scale(x_data)
    xMat = numpy.mat(x_data)
    ws = numpy.mat(ws)
    return [1 if x>=0.5 else 0 for x in sigmoid(xMat*ws)]
predictions = predict(X_data,ws)
print(classification_report(y_data,predictions))


