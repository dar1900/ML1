import graphviz
from matplotlib import pyplot
import numpy
from sklearn.metrics import classification_report
from sklearn import tree
from sklearn.model_selection import train_test_split


# 载入数据
data=numpy.genfromtxt('../data/LR-testSet2.txt',delimiter=',')
x_data=data[:,:-1]
y_data=data[:,-1]
pyplot.scatter(x_data[:,0],x_data[:,1],c=y_data)
# pyplot.show()


# 分割数据,默认四分之三分割
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data)
# 创建决策树模型
# max_depth，树的深度
# min_samples_split内部节点划分所需要最小样本数
model = tree.DecisionTreeClassifier(max_depth=4,min_samples_split=4)
# 输入数据建立模型
model.fit(x_train,y_train)


# 导出决策树
dot_data=tree.export_graphviz(model,
                              out_file=None,
                              feature_names=['x','y'],
                              filled=True,
                              rounded=True,
                              special_characters=True)
# graph = graphviz.Source(dot_data)


# 画图
# 获取数据值所在的范围
x_min,x_max = x_data[:,0].min()-1,x_data[:,0].max()+1
y_min,y_max = x_data[:,1].min()-1,x_data[:,1].max()+1
# 生成网络矩阵
xx,yy=numpy.meshgrid(numpy.arange(x_min,x_max,0.02),
                     numpy.arange(y_min,y_max,0.02))
z=model.predict(numpy.c_[xx.ravel(),yy.ravel()])
# ravel与flatten类似，多维数据转一维，。flatten不会改变原始数据，ravel会改变原始数据
z=z.reshape(xx.shape)
# 等高线图
cs=pyplot.contourf(xx,yy,z)
pyplot.scatter(x_data[:,0],x_data[:,1],c=y_data)
pyplot.show()

predictions =model.predict(x_train)
print(classification_report(predictions,y_train))
predictions =model.predict(x_test)
print(classification_report(predictions,y_test))