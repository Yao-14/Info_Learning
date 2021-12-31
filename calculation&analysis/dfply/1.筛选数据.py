from dfply import *
import pandas as pd
data = pd.read_excel('example_file.xlsx',header=None)
data.columns=['Chr','Start','End']
print(data)
#1.select()：筛选需要的列————select(X.Chr, X.Start),选择列标签为Chr、Start的列
df1 = data >> select(X.Chr, X.Start)
print(df1)
#2.select(~X.)：筛选出除了放置波浪号的列以外的列————select(~X.Start,~X.End),选择列标签不为Start、End的列
df2 = data >> select(~X.Start,~X.End)
print(df2)
#3.head()：选择需要的行————head(10)，选择前十行数据
df3 = data >> select(X.Chr, X.Start, X.End) >> head(10)
print(df3)
#4.tail()：tail(3)————选择最后三行。head(10) >> tail(3))————选择前十行的最后三行，即第8、9、10行
df4 = data >> select(X.Chr, X.Start, X.End) >> head(10) >> tail(3)
print(df4)
#5.mask()————筛选数据，根据逻辑条件在pandas DataFrame中选择行的子集
df5 = data >> mask(X.Chr == 'Chr2',  X.Start >1000, X.End < 100000)
print(df5)
#6.pull()————适用于如果只想要python在管道函数的最后返回pandas数据中的一列。
df6 = data >> mask(X.Chr == 'Chr2',  X.Start >1000, X.End < 100000) >> pull(X.Start)
print(df6)
#7.上述多个函数合用————若要换行需要加个括号
df7 = (data >> select(X.Chr, X.Start) >>
       mask(X.Chr == 'Chr2',  X.Start >10000) >>
       head(3))
print(df7)
