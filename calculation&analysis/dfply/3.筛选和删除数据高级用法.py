'''
更高级的筛选和删除————以下功能用于select和drop功能中，并可与〜一起使用。
列：
starts_with（prefix）：查找以字符串前缀开头的列。
ends_with（suffix）：查找以字符串后缀结尾的列。
contains（substr）：查找名称中包含子字符串的列。
everything（）：所有列。
columns_between（start_col，end_col，inclusive = True）：查找指定的开始列和结束列之间的列。包含性布尔关键字参数指示是否应包含结束列。
columns_to（end_col，inclusive = True）：获取指定结束列的列。包含参数指示是否应包括结束列。
columns_from（start_col）：获取从指定列开始的列。
行：
row_slice（）：可以使用row_slice（）函数选择切片行。 可以传递单个整数索引或索引列表来选择行。 这与使用pandas包的的.iloc功能相同。
sample（）：函数的功能与DataFrames的pandas.sample（）方法完全相同
distinct()：选择唯一行
'''

from dfply import *
import pandas as pd
data = pd.read_excel('example_file.xlsx',header=None)
data.columns=['Chr','Start','End']
#1.starts_with（prefix）：查找以字符串前缀开头的列;
#2.ends_with（suffix）：查找以字符串后缀结尾的列。
df1 = data >> select(starts_with('Ch'),ends_with('r'))
print(df1)
#3.contains（substr）：查找名称中包含子字符串的列。
df3 = data >> select(contains('t'))
print(df3)
#4.columns_between（start_col，end_col，inclusive = True）：查找指定的开始列和结束列之间的列。inclusive指示是否应包含结束列。
df4 = data >> select(columns_between(X.Chr,X.Start,inclusive=True))
print(df4)
#5.row_slice（[0,10，20]）：输出第1行、第10行和第20行。 可以传递单个整数索引或索引列表来选择行。
df5 = data >> row_slice([0,10])
print(df5)
#6.row_slice（9）：输出第9行
df6 = data >> row_slice(9)
print(df6)
#7.sample（）：随机数据n行数据
df7 = data >> sample(n= 5, replace=False)
print(df7)
#8.distinct()：选择唯一行————即比如Chr一列有4个Chr1，4个Chr2，则输出一个Chr1和一个Chr2
df8 = data >> distinct(X.Chr)
print(df8)