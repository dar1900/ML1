import pandas
import re

list1 = ["482875","483114","483181"]
list2 = ["津天士力","辽宁仙鹤"]

file_path = 'C:\\Users\\73573\\Desktop\\沈总\\2月\\483181.txt'
file = 'C:\\Users\\73573\\Desktop\\沈总\\2月\\result_483181.txt'
with open(file_path,encoding='gbk') as f:
    file_handle = open(file, 'a', encoding='utf-8')
    for i, line in enumerate(f.readlines()):
        # i 是行数
        # line 是每行的字符串，可以使用 line.strip().split(",") 按分隔符分割字符串
        # if line.strip().split(",")[0] in list1 and line.strip().split(",")[4] in list2:
            # file_handle.write(line)
        if (i+2)%2 == 1:
            file_handle.write(line.strip('\n'))
            print(i)
        if i%2 ==0 :
            file_handle.write(line)
            print(i)



    file_handle.close()
    f.close()





