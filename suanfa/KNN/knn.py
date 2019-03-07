import numpy
import operator
from matplotlib import pyplot

# 已知分类的数据


x1=numpy.array([3,2,1])
y1=numpy.array([104,100,81])
x2=numpy.array([101,99,98])
y2=numpy.array([10,5,2])
scatter1=pyplot.scatter(x1,y1,c='r')
scatter2=pyplot.scatter(x2,y2,c='b')
# 位置数据
x=numpy.array([18])
y=numpy.array([90])
scatter3=pyplot.scatter(x,y,c='k')
# 画图例
pyplot.legend(handles=[scatter1,scatter2,scatter3],labels=['labelA','labelB','X'],loc='best')
pyplot.show()


# 已知分类的数据
x_data=numpy.array([[3,104],
                    [2,100],
                    [1,81],
                    [101,10],
                    [99,5],
                    [81,2]])
y_data=numpy.array(['A','A','A','B','B','B'])
x_test=numpy.array([18,90])


# 计算样本数量
x_data_size = x_data.shape[0]
print("x_data_size:",x_data_size)
# 复制x_test
numpy.tile(x_test,(x_data_size,1))
# 计算x_test与每一个样本的插值
diffMat=numpy.tile(x_test,(x_data_size,1))-x_data
print("diffMat:",diffMat)
# 计算插值的平方
sqDiffMat = diffMat**2
print("sqDiffMat:",sqDiffMat)
# 求和
sqDistances = sqDiffMat.sum(axis=1)
print("sqDistances:",sqDistances)
# 开放
distances = sqDistances**0.5
print("distances:",distances)
# 从小到大排序,是对索引排序
sortedDistances = distances.argsort()
print("sortedDistances:",sortedDistances)


classCount = {}
# 设置k
k=5
for i in range(k):
    # 获取标签
    votelabel = y_data[sortedDistances[i]]
    # 统计标签数量
    classCount[votelabel]=classCount.get(votelabel,0)+1
print(classCount)


# 根据operator.intemgetter(1)-第1个值对classCount排序，然后再取倒序
sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
print("sortedClassCount:",sortedClassCount)
# 获取数量最多的标签
knnclass = sortedClassCount[0][0]
print("knnclass:",knnclass)