import pymssql

import numpy
import pandas
import pyecharts

server = "localhost"
user = "sa"
password = "sa"

conn = pymssql.connect(server,user,password,"yy")
cursor = conn.cursor(as_dict=True)  #获取光标

cursor.execute('select * from mat_every')
data = cursor.fetchall()
conn.close()
# data_matrix=numpy.mat(data)
data_array=numpy.array(data)
# print(data_array)
data_df=pandas.DataFrame(index=numpy.arange(0,len(data_array)),columns=['year','month','area','date','mat'])
for i in range(0,len(data_array)):
    data_df.loc[i,'year']=data_array[i]['年']
    data_df.loc[i, 'month'] = data_array[i]['月']
    data_df.loc[i, 'area'] = data_array[i]['销售区组']
    data_df.loc[i, 'date'] = str(int(data_array[i]['年']))+'年'+str(int(data_array[i]['月']))+'月'
    data_df.loc[i, 'mat'] = data_array[i]['mat']
# print(data_df)
data_df=data_df.sort_values(by=['date'],ascending=True)
# print(data_df)
x=data_df['date'].values
y=data_df['mat'].values
z=data_df['area'].values
z=list(set(z))
# print(z)
line = pyecharts.Line("MAT",'2019-01-14',width=1200,height=600)
for i in range(len(z)):
    for j in range(data_df.shape[0]):
        # print(data_df.ix[j,'area'])
        if data_df.ix[j,'area']==z[i]:
            line.add( x, y, is_datazoom_show=True)
line.render('mat.html')



