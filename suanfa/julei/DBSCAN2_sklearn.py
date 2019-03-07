from sklearn.cluster import DBSCAN, KMeans
import numpy
from matplotlib import pyplot
from sklearn import datasets


x1,y1=datasets.make_circles(n_samples=2000,factor=0.5,noise=0.05)
x2,y2 = datasets.make_blobs(n_samples=1000,centers=[[1.2,1.2]],cluster_std=[[.1]])
x=numpy.concatenate((x1,x2))
pyplot.scatter(x[:,0],x[:,1],marker='o')
pyplot.show()

y_pred =KMeans(n_clusters=3).fit_predict(x)
pyplot.scatter(x[:,0],x[:,1],c=y_pred)
pyplot.show()

y_pred =DBSCAN(eps=0.2,min_samples=50).fit_predict(x)
pyplot.scatter(x[:,0],x[:,1],c=y_pred)
pyplot.show()