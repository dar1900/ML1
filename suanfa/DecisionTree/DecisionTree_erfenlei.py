import graphviz
from matplotlib import pyplot
import numpy
from sklearn.metrics import classification_report
from sklearn import tree


# 载入数据

# data=numpy.genfromtxt('D:\乐哥暂存资料\shijinle_bianchengyuju\python\ML_1\LogisticRegression\LR-testSet.csv',delimiter=',')
data=numpy.genfromtxt('../LogisticRegression/LR-testSet.csv',delimiter=',')
x_data = data[:,:-1]
y_data = data[:,-1]
pyplot.scatter(x_data[:,0],x_data[:,1],c=y_data)
pyplot.show()


# 创建决策树模型
model = tree.DecisionTreeClassifier()
# 输入数据建立模型
model.fit(x_data,y_data)

# 导出决策树
dot_data = tree.export_graphviz(model,
                                out_file=None,
                                feature_names=['x','y'],
                                class_names=['label0','label1'],
                                filled=True,
                                rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
# graph.view()

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

predictions =model.predict(x_data)
print(classification_report(predictions,y_data))