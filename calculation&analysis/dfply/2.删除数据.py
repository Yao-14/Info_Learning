from dfply import *
import pandas as pd
data = pd.read_excel('example_file.xlsx',header=None)
data.columns=['Chr','Start','End']

#1.drop():drop(X.End)————删除某一列数据
df1 = data >> drop(X.End)
print(df1)
#2.drop(~X.)：删除除了放置波浪号的列以外的列————drop(~X.Start,~X.End),删除列标签不为Start、End的列
df1 = data >> drop(~X.Start,~X.End)
print(df1)
#3.多个函数合用————若要换行需要加个括号
df2= (data >>
      mask(X.Chr == 'Chr2',  X.Start >1000, X.End < 100000) >>
      drop(X.End))
print(df2)
