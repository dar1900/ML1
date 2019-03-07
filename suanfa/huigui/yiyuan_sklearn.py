import numpy
from sklearn.linear_model import LinearRegression
import pandas
from matplotlib import pyplot



# 载入数据
data=pandas.read_csv("data.csv",delimiter=",")
data.columns=['a','b']
x_data=data["a"].values
y_data=data["b"].values
# pyplot.scatter(x_data,y_data)
# pyplot.show()
print(x_data.shape)

# 处理数据类型
x_data=pandas.DataFrame(x_data.reshape(x_data.shape[0],1))
y_data=pandas.DataFrame(y_data.reshape(y_data.shape[0],1))
print(x_data.shape,y_data.shape)
# x_data=data[:,0,numpy.newaxis]
# y_data=data[:,1,numpy.newaxis]
# 创建并拟合模型
model = LinearRegression()
model.fit(x_data,y_data)


# 画图
pyplot.plot(x_data,y_data,'b.')
pyplot.plot(x_data,model.predict(x_data),'r')
pyplot.show()
