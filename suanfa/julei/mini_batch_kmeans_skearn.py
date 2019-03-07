from sklearn.cluster import MiniBatchKMeans
import numpy
from matplotlib import pyplot

data = numpy.genfromtxt("../data/kmeans.txt",delimiter=" ")
# 设置k值
k=4

# 训练模型
model = MiniBatchKMeans(n_clusters=k)
model.fit(data)

# 分类中心点坐标
centers = model.cluster_centers_
print(centers)
# 预测结果
result =model.predict(data)
print(result)
# model.labels_

# 画出各个数据点，用不同颜色表示分类
mark = ['or','ob','og','oy']
for i,d in enumerate(data):
    pyplot.plot(d[0],d[1],mark[result[i]])
# 画出各个分类的中心点
mark = ['*r','*b','*g','*y']
for i,center in enumerate(centers):
    pyplot.plot(center[0],center[1],mark[i],markersize=20)
pyplot.show()

# 获取数值所在的范围
x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1
y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1
# 生成网格矩阵
xx, yy = numpy.meshgrid(numpy.arange(x_min, x_max, 0.02),
                        numpy.arange(y_min, y_max, 0.02))
z = model.predict(numpy.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)
# 等高线图
cs = pyplot.contourf(xx, yy, z)
# 显示结果
# 画出各个数据点，用不同颜色表示分类
mark = ['or','ob','og','oy']
for i,d in enumerate(data):
    pyplot.plot(d[0],d[1],mark[result[i]])
# 画出各个分类的中心点
mark = ['*r','*b','*g','*y']
for i,center in enumerate(centers):
    pyplot.plot(center[0],center[1],mark[i],markersize=20)
pyplot.show()