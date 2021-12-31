from dfply import *
import pandas as pd
data = pd.read_excel('example_file.xlsx',header=None)
data.columns=['Chr','Start','End']

#1.mutate()————可以使用mutate()函数创建新变量,并且可以在一次调用中创建多个变量同时保留原变量
df1 = data >> mutate(Size=X.End-X.Start)
print(df1)
#2.transmute()————可以使用transmute()函数创建新变量,但不保留原变量
df2 = data >> transmute(Size=X.End-X.Start)
print(df2)
