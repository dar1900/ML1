from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split


news = fetch_20newsgroups(subset='all')
print(news.target_names)
print(len(news.data))
print(len(news.target))
print(news.data[0])
print(news.target[0])
print(news.target_names[news.target[0]])

x_train,x_test,y_train,y_test = train_test_split(news.data,news.target)


# CountVectorizer方法构建单词的字典，每个单词实例被转换为特征向量的一个数值特征，
# 每个元素是特定单词在文本中出现的次数
texts=["dog cat fish","dog cat cat","fish bird","bird"]
cv=CountVectorizer()
cv_fit = cv.fit_transform(texts)
#
print(cv.get_feature_names())
print(cv_fit.toarray())
print(cv_fit.toarray().sum(axis=0))