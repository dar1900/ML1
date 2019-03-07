import numpy
from matplotlib import pyplot

# 输入数据
X = numpy.array([[1, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 1],
                 [1, 1, 0,1, 0, 0],
                 [1, 1, 1, 1, 1, 1]])
# 标签
Y = numpy.array([-1, 1, 1, -1])
# 权值初始化，3行1列(对应几行输入，几列输出)，取值范围-1到1
W = (numpy.random.random(6) - 0.5) * 2
print(W)
# print(X.shape,(W.T).shape)
# 学习率设置
lr = 0.11
# 计算迭代次数
n = 0
# 神经网络输出
O = 0


def update():
    global X, Y, W, lr, n
    n += 1
    O = numpy.dot(X, W.T)
    W_C = lr * ((Y - O.T).dot(X)) / int(X.shape[0])
    W = W + W_C


for i in range(1000):
    update()  # 更新权值
print(W)
print(numpy.dot(X, W.T))
# 正样本
x1 = [0, 1]
y1 = [1, 0]
# 负样本
x2 = [0, 1]
y2 = [0, 1]


def calculate(x, root):
    a = W[5]
    b = W[2] + x * W[4]
    c = W[0] + x * W[1] + x * x * W[3]
    if root == 1:
        return (-b + numpy.sqrt(b * b - 4 * a * c)) / (2 * a)
    if root == 2:
        return (-b - numpy.sqrt(b * b - 4 * a * c)) / (2 * a)


xdata = numpy.linspace(-1, 2)
pyplot.figure()
pyplot.plot(xdata, calculate(xdata, 1), 'r')
pyplot.plot(xdata, calculate(xdata, 2), 'r')
pyplot.plot(x1, y1, 'bo')
pyplot.plot(x2, y2, 'yo')
pyplot.show()
