#SVM低维映射到高维
from matplotlib import pyplot
from sklearn import datasets
from mpl_toolkits.mplot3d import Axes3D


x_data,y_data = datasets.make_circles(n_samples=500,factor=.3,noise=.10)
pyplot.scatter(x_data[:,0],x_data[:,1],c=y_data)
pyplot.show()
z_data = x_data[:,0]**2+x_data[:,1]**2
ax=pyplot.figure().add_subplot(111,projection='3d')
ax.scatter(x_data[:,0],x_data[:,1],z_data,c=y_data,s=100)   #点为红色三角形
#显示图像
pyplot.show()
