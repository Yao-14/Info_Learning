
'''

import pandas as pd

# read 输入文件的设置
sep = ''        若输出的元素是一个元素，可添加sep = '|'将元素拆分分多个序列
na_values=0     表示若文件中有缺失值则会填充为0
header = None   若第一行是需要的数据而不是作为列标签，可以添加header = None，并添加name = ['','','']来添加想要的列标签
index_col=0     设置行标签为那一列数据，0表示第一列作为行标签
nrows = n       若不需要文件的所有数据，添加nrows = 数字，来获得想要的前n行数据
usecols = []    若不需要文件的所有数据，添加usecols = 列名列表，来获取的某些列数据
sheet_name = 'sheet1'   一个excel中可能含有多个sheet表格，因此为获得想要打开的那个sheet，可以添加sheet_name = 'sheet1'
sheet_name = [0,1]      若想要同时将获得一个excel中的多个sheet，可以通过sheet_name = [0,1],输出结果是一个字典，字典中包含了两个dataframe

# to 输出文件设置
header = False                  输出若不需要列标签则添加header = False
index = False                   输出若不需要行标签则添加index = False
encoding = 'utf-1.Bar-sig'      若输出的csv文件在excel中打开出现乱码现象，可以添加encoding ='utf-1.Bar-sig'从而生成一个excel可以正常打开的无bom头的csv文件

'''
