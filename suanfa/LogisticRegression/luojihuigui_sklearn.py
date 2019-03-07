import numpy
from matplotlib import pyplot
from numpy import genfromtxt
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.metrics import classification_report

# 数据是否标准化
scale = False

# 读取数据
data = genfromtxt("LR-testSet.csv", delimiter=",")
x_data = data[:, :-1]
y_data = data[:, -1]


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

# 创建模型
logistic = linear_model.LogisticRegression()
logistic.fit(x_data, y_data)
# 模型参数
print("logistic.coef_:",logistic.coef_)
# 如果做了数据标准化就不画图，不做可以画图
if scale == False:
    #     画图决策边界
    plot()
    x_test = numpy.array([[-4], [3]])
    y_test = (-logistic.intercept_ - x_test * logistic.coef_[0][0]) / logistic.coef_[0][1]
    pyplot.plot(x_test, y_test, 'k')
    pyplot.show()

# 预测，混淆矩阵
predictions = logistic.predict(x_data)
print(classification_report(y_data, predictions))
