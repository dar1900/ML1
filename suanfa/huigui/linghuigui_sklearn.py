import numpy
from matplotlib import pyplot
from numpy import genfromtxt
from sklearn import linear_model



# 读取数据
data = genfromtxt(r"longley.csv",delimiter=',')
print(data)


# 切分数据
x_data = data[1:,2:]
y_data = data[1:,1]
print(x_data)
print(y_data)


# 创建模型
# 生产50个值
alphas_to_test = numpy.linspace(0.001,1)    #linspace方法默认生成50个值
# 创建模型，保存误差值
model = linear_model.RidgeCV(alphas=alphas_to_test,store_cv_values=True)    #CV是交叉验证
model.fit(x_data,y_data)
# 岭系数
print("alpha=",model.alpha_)
# loss值
print("cv_values_.shape=",model.cv_values_.shape)
#cv_values_.shape= (16, 50) 16是16个样本数据，50是50个岭系数


# 画图
# 岭系数跟loss值得关系
pyplot.plot(alphas_to_test,model.cv_values_.mean(axis=0))
# 读取的岭系数值的位置
pyplot.plot(model.alpha_,min(model.cv_values_.mean(axis=0)),'ro')
pyplot.show()


# 预测，传入二位数组
model.predict(x_data[2,numpy.newaxis])

