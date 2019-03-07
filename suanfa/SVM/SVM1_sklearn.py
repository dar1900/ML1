from sklearn import svm


x=[[3,3],[4,3],[1,1]]
y=[1,1,-1]

model =svm.SVC(kernel='linear')     #核函数
model.fit(x,y)

# 打印支持向量
print(model.support_vectors_)
# 第2和第0个点是支持向量机
print(model.support_)
# 有几个支持向量
print(model.n_support_)
model.predict([[4,3]])
model.coef_     #w,b两个参数
model.intercept_    #截距或者成为偏置值