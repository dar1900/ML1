import pandas
import re

list1 = ["482875","483114","483181"]
list2 = ["津天士力","辽宁仙鹤"]

file_path = 'D:\\dz\\2019年BMS特定销售供应商补偿协议功能数据.txt'
file = 'result.txt'
with open(file_path,encoding='gbk') as f:
    file_handle = open('info.txt', 'a', encoding='utf-8')
    for i, line in enumerate(f.readlines()):
        # i 是行数
        # line 是每行的字符串，可以使用 line.strip().split(",") 按分隔符分割字符串
        if line.strip().split(",")[0] in list1 and line.strip().split(",")[4] in list2:
            file_handle.write(line)
            print(i, line)
    file_handle.close()
    f.close()





