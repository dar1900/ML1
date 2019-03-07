# 导入算法包以及数据集
from sklearn import neighbors,datasets,tree
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
import numpy
from matplotlib import pyplot


iris = datasets.load_iris()
x_data = iris.data[:,:2]
y_data = iris.target
x_train,x_test,y_train,y_test = train_test_split(x_data,y_data)

knn = neighbors.KNeighborsClassifier()
knn.fit(x_train,y_train)


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

# 画图，等高线
plot(knn)
# 样本散点图
pyplot.scatter(x_data[:,0],x_data[:,1],c=y_data)
pyplot.show()
# 准确率
knn.score(x_test,y_test)

# 决策树
dtree=tree.DecisionTreeClassifier()
dtree.fit(x_train,y_train)
# 样本散点图
plot(dtree)
pyplot.scatter(x_data[:,0],y_data[:,1],c=y_data)
pyplot.show()
# 准确率
dtree.score(x_test,y_test)


# bagging+knn
bagging_knn = BaggingClassifier(knn,n_estimators=100)
bagging_knn.fit(x_train,y_train)
plot(bagging_knn)
# 样本散点图
pyplot.scatter(x_data[:,0],x_data[:,1],c=y_data)
pyplot.show()
bagging_knn.score(x_test,y_test)

# bagging+tree
bagging_tree=BaggingClassifier(tree,n_estimators=100)
# 输入数据建立模型
bagging_tree.fit(x_train,y_train)
plot(bagging_tree)
# 样本散点图
pyplot.scatter(x_data[:,0],x_data[:,1],c=y_data)
pyplot.show()
bagging_tree.score(x_test,y_test)