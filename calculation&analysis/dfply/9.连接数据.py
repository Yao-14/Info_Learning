'''
bind()函数有类似于pandas.concat() 这样在行和列上用于合并数据框的。
bind_rows(other, join='outer', ignore_index=False)在竖直方向合并数据框.
bind_cols(other, join='outer', ignore_index=False)在水平方向合并数据框
'''
from dfply import *
import pandas as pd
a = pd.DataFrame({
        'x1':['A','B','C'],
        'x2':[1,2,3]})
b = pd.DataFrame({
    'x1':['A','B','D'],
    'x3':[True,False,True]})

print(a >> bind_rows(b, join='outer',ignore_index=True))
print(a >> bind_cols(b, join='outer',ignore_index=True))