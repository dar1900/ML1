import numpy
from matplotlib import pyplot

# 载入数据
data = numpy.genfromtxt("../data/kmeans.txt",delimiter=" ")
pyplot.scatter(data[:,0],data[:,1])
pyplot.show()
print(data.shape)

                        #训练模型
# 计算距离
def euclDistance(vector1,vector2):
    return numpy.sqrt(sum(vector2-vector1)**2)
# 初始化质心
def initCentroids(data,k):
    numSamples,dim = data.shape
    # k个质心，列数跟样本的列数一样
    centroids = numpy.zeros((k,dim))
    # 随机选出k个质心
    for i in range(k):
        # 随机选出一个样本的索引
        index = int(numpy.random.uniform(0,numSamples))
        # 作为初始化的质心
        centroids[i,:]=data[index,:]
    return centroids
# 传入数据集和k值
def kmeans(data,k):
    # 计算样本个数
    numSamples = data.shape[0]
    # 样本的属性，第一列保存该样本属于哪个簇，第二列保存该样本跟它所属簇的误差
    clusterData = numpy.array(numpy.zeros((numSamples,2)))
    # 决定质心是否改变的变量
    clusterChanged = True
    # 初始化质心
    centorids = initCentroids(data,k)
    while clusterChanged:
        clusterChanged=False
        # 循环每一个样本
        for i in range(numSamples):
            # 最小距离
            minDist = 100000.0
            # 定义样本所属的簇
            minIndex = 0
            # 循环每一个质心和样本，计算距离
            for j in range(k):
                distance = euclDistance(centorids[j,:],data[i,:])
                # 如果计算的距离小于最小距离，则更新最小距离
                if distance<minDist:
                    minDist = distance
                    # 更新最小距离
                    clusterData[i,1]=minDist
                    # 更新样本所属的簇
                    minIndex=j
            # 如果样本的所属的簇发生了变化
            if clusterData[i,0] != minIndex:
                # 质心要重新计算
                clusterChanged = True
                # 更新样本的簇
                clusterData[i,0] = minIndex
        # 更新质心
        for j in range(k):
            # 获取第j个簇所有的样本所在的索引
            cluster_index = numpy.nonzero(clusterData[:,0]==j)
            # 第j个簇所有的样本点
            pointsInCluster = data[cluster_index]
            # 计算质心
            centorids[j,:] = numpy.mean(pointsInCluster,axis=0)
            # showCluster(data,k,centorids,clusterData)
    return centorids,clusterData

# 显示结果
def showCluster(data, k, centroids, clusterData):
    numSamples,dim = data.shape
    if dim !=2:
        print("dimension of your data is not 2!")
        return 1
    # 用不同颜色形状来表示各个类别
    mark = ['or','ob','og','ok','^r','+r','sr','dr','<r','pr']
    if k>len(mark):
        print("Your k is too large!")
        return 1
    # 画样本点
    for i in range(numSamples):
        markIndex = int(clusterData[i,0])
        pyplot.plot(data[i,0],data[i,1],mark[markIndex])
    # 用不同颜色形状来表示各个类别
    mark = ['*r','*b','*g','*k','^b','+b','sb','db','<b','pb']
    # 画质心
    for i in range(k):
        pyplot.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize=20)
    pyplot.show()

# 设置k值
k=4
min_loss =10000
min_loss_centroids = numpy.array([])
min_loss_clusterData = numpy.array([])
for i in range(50):
    # centroids 簇的中心点
    # cluster Data 样本的属性，第一列保存该样本属于哪个簇，第二列保存该样本跟他所属簇的误差
    centroids,clusterData = kmeans(data,k)
    loss = sum(clusterData[:,1])/data.shape[0]
    if loss<min_loss:
        min_loss=loss
        min_loss_centroids = centroids
        min_loss_clusterData = clusterData

print('cluster complete!')
centroids = min_loss_centroids
clusterData = min_loss_clusterData
# 显示结果
showCluster(data,k,centroids,clusterData)