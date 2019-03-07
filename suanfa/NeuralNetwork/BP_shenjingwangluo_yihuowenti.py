import numpy
from matplotlib import pyplot


# 输入数据
X=numpy.array([[1,0,0],
               [1,0,1],
               [1,1,0],
               [1,1,1]])
# 标签
Y = numpy.array([[0, 1, 1, 0]])
# 权值初始化，几行几列(对应几行输入，几列输出)，取值范围-1到1
V= numpy.random.random((3,4))*2-1
W = numpy.random.random((4,1))*2-1
print(V,W)
# print(X.shape,(W.T).shape)
# 学习率设置
lr = 0.11
# 神经网络输出
O = 0

def sigmoid(x):
    return 1/(1+numpy.exp(-x))
def dsigmoid(x):
    return x*(1-x)
def update():
    global X,Y,W,V,lr
    L1 = sigmoid(numpy.dot(X,V))    #隐藏层输出（4,4）
    L2 = sigmoid(numpy.dot(L1,W))   #输出层输出（4,1）

    L2_delta = (Y.T-L2)*dsigmoid(L2)
    L1_delta = L2_delta.dot(W.T)*dsigmoid(L1)

    W_C = lr*L1.T.dot(L2_delta)
    V_C = lr*X.T.dot(L1_delta)

    W=W+W_C
    V=V+V_C
for i in range(20000):
    update()    #更新权值
    if i %500==0:
        L1 = sigmoid(numpy.dot(X, V))  # 隐藏层输出（4,4）
        L2 = sigmoid(numpy.dot(L1, W))  # 输出层输出（4,1）
        print('Error:',numpy.mean(numpy.abs(Y.T-L2)))
L1 = sigmoid(numpy.dot(X, V))  # 隐藏层输出（4,4）
L2 = sigmoid(numpy.dot(L1, W))  # 输出层输出（4,1）
print(L2)
def judge(x):
    if x>=0.5:
        return 1
    else:
        return 0
for i in map(judge,L2):
    print(i)