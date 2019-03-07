from matplotlib import pyplot
import numpy
from sklearn.metrics import classification_report
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# 载入数据
data=numpy.genfromtxt('../data/LR-testSet2.txt',delimiter=',')
x_data=data[:,:-1]
y_data=data[:,-1]
pyplot.scatter(x_data[:,0],x_data[:,1],c=y_data)
# pyplot.show()

x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.5)
def plot(model):
    # 获取数据值所在的范围
    x_min, x_max = x_data[:, 0].min() - 1, x_data[:, 0].max() + 1
    y_min, y_max = x_data[:, 1].min() - 1, x_data[:, 1].max() + 1
    # 生成网络矩阵
    xx, yy = numpy.meshgrid(numpy.arange(x_min, x_max, 0.02),
                            numpy.arange(y_min, y_max, 0.02))
    z = model.predict(numpy.c_[xx.ravel(), yy.ravel()])
    # ravel与flatten类似，多维数据转一维，。flatten不会改变原始数据，ravel会改变原始数据
    z = z.reshape(xx.shape)
    # 等高线图
    cs = pyplot.contourf(xx, yy, z)
    pyplot.scatter(x_test[:, 0], x_test[:, 1], c=y_test)
    pyplot.show()


dtree=tree.DecisionTreeClassifier()
dtree.fit(x_train,y_train)
plot(dtree)
dtree.score(x_test,y_test)

RF=RandomForestClassifier(n_estimators=50)
RF.fit(x_train,y_train)
plot(RF)
RF.score(x_test,y_test)