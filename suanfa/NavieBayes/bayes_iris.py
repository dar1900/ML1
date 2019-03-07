import numpy
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.naive_bayes import MultinomialNB,BernoulliNB,GaussianNB


# 载入数据集
iris = datasets.load_iris()
x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target)

# mul_nb=MultinomialNB()
mul_nb=GaussianNB() #处理连续型数据效果会好一点
mul_nb.fit(x_train,y_train)
print(classification_report(mul_nb.predict(x_test),y_test))
print(confusion_matrix(mul_nb.predict(x_test),y_test))