from dfply import *
import pandas as pd
data = pd.read_excel('example_file.xlsx',header=None)
data.columns=['Chr','Start','End']
#cumsum(X.Size)：计算列的累计和
df1 = data >> mutate(Size=X.End-X.Start) >> mutate(Size_cumsum=cumsum(X.Size)) >> head(5)
print(df1)
#cummean(X.Size)：计算列的累积平均值
df2 = data >> mutate(Size=X.End-X.Start) >> mutate(Size_cummean=cummean(X.Size)) >> head(5)
print(df2)
#cummax(X.Size)：计算列的累积最大值。
df3 = data >> mutate(Size=X.End-X.Start) >> mutate(Size_cumax=cummax(X.Size)) >> head(5)
print(df3)
#cummin(X.Size)：计算列的累积最小值。
df4 = data >> mutate(Size=X.End-X.Start) >> mutate(Size_cummin=cummin(X.Size)) >> head(5)
print(df4)
#cumprod(X.Size)：计算列累积乘积。
df5 = data >> mutate(Size=X.End-X.Start) >> mutate(Size_cumprod=cumprod(X.Size)) >> head(5)
print(df5)