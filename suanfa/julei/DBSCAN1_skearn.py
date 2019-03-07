from sklearn.cluster import DBSCAN
import numpy
from matplotlib import pyplot

# 载入数据
data = numpy.genfromtxt("../data/kmeans.txt",delimiter=" ")

# 训练模型
# eps距离阙值，min_samples核心对象在eps领域的样本数阙值
model = DBSCAN(eps=1,min_samples=4)
model.fit(data)

result = model.fit_predict(data)
print(result,result.dtype)

# 画出各个数据点，用不同颜色表示分类
mark = ['or','ob','og','oy','ok','om']
for i,d in enumerate(data):
    pyplot.plot(d[0],d[1],mark[result[i]])
pyplot.show()