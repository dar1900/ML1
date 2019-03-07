'''
异或
0~0=0
0~1=1
1~0=1
1~1=0
'''
import numpy
from matplotlib import pyplot


# 输入数据
X=numpy.array([[1,0,0],
               [1,0,1],
               [1,1,0],
               [1,1,1]])
# 标签
Y=numpy.array([[-1],
               [1],
               [1],
               [-1]])
# 权值初始化，3行1列，取值范围-1到1
W=(numpy.random.random([3,1])-0.5)*2
print(W)
# 学习率设置
lr=0.11
# 神经网络输出
O=0
def update():
    global X,Y,W,lr
    O=numpy.sign(numpy.dot(X,W))    #shape:(3,1)
    W_C= lr*(X.T.dot(Y-O))/int(X.shape[0])
    W=W+W_C

for i in range(100):
    update()
    print(W)
    print(i)
    O=numpy.sign(numpy.dot(X,W))
    if(O==Y).all():
        print('Finished')
        print('epoch:',i)
        break
# 正样本
x1=[0,1]
y1=[1,0]
# 负样本
x2=[0,1]
y2=[0,1]
# 计算分界线的斜率以及截距
k=-W[1]/W[2]
d=-W[0]/W[2]
print('k=',k)
print('d=',d)
xdata=(-2,3)
pyplot.figure()
pyplot.plot(xdata,xdata*k+d,'r')
pyplot.scatter(x1,y1,c='b')
pyplot.scatter(x2,y2,c='y')
pyplot.show()