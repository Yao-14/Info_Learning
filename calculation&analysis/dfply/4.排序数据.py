from dfply import *
import pandas as pd
data = pd.read_excel('example_file.xlsx',header=None)
data.columns=['Chr','Start','End']

#1.arrange():arrange()可根据一列或多列来排序行; 默认行为是按升序对行进行排序。例如，先按Chr，再按Start排序
df1 = data >> arrange(X.Chr,X.Start) >> head(5)
print(df1)
#2.ascending=False:降序
df2 = data >> arrange(X.Chr,X.Start,ascending=False) >> head(5)
print(df2)