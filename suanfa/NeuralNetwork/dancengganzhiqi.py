import numpy
from matplotlib import pyplot


# 输入数据
X=numpy.array([[1,3,3],
               [1,4,3],
               [1,1,1],
               [1,0,2]])
# 标签
Y=numpy.array([[1],
               [1],
               [-1],
               [-1]])
# 权值初始化，3行1列(对应几行输入，几行输出)，取值范围-1到1
W=(numpy.random.random([3,1])-0.5)*2
print(W)
# 学习率设置
lr=0.11
# 神经网络输出
O=0
def update():
    global X,Y,W,lr
    # 单层神经网络与线性神经网络不同的是激活函数
    # 下面是单层神经网络的激活函数：
    O=numpy.sign(numpy.dot(X,W))    #shape:(3,1)
    # 下面是线性神经网络的激活函数：
    # O=numpy.dot(X,W)    #shape:(3,1)
    W_C= lr*(X.T.dot(Y-O))/int(X.shape[0])
    W = W +W_C


for i in range(100):
    update()    #更新权值
    print(W)    #打印当前权值
    print(i)    #打印当前迭代次数
    O=numpy.sign(numpy.dot(X,W))    #计算当前输出
    if(O == Y).all():   #如果实际输出等于期望输出，模型收敛，循环结束
        print('Finished')
        print('epoch:',i)
        break
# 正样本
x1=[3,4]
y1=[3,3]
# 负样本
x2=[1,0]
y2=[1,2]
# 计算分界线的斜率以及截距
k=-W[1]/W[2]
d=-W[0]/W[2]
print('k=',k)
print('d=',d)
xdata = (0,5)
pyplot.figure()
pyplot.plot(xdata,xdata*k+d,'r')
pyplot.scatter(x1,y1,c='b')
pyplot.scatter(x2,y2,c='y')
pyplot.show()

