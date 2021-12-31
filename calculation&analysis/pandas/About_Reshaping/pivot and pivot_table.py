'''
Dataframe.pivot(values=None, index=None, columns=None)
    :通过指定的索引和列对数据进行重塑生成透视表，但无法聚合。（即若有重复项会报错，所以一般不使用）

Dataframe.pivot_table(values=None, index=None, columns=None, aggfunc='mean', fill_value=None)
    :通过指定的索引和列对数据进行重塑生成透视表，可以聚合(aggfunc处理重复项）。（一般使用，耗内存适合小数据使用）

对于大数据，pivot_table占用内存过于巨大并且速度较慢，因此不适合，可以选择以下两种方式：
1. groupby+unstack
2. 稀疏矩阵压缩格式csr_matrix

'''
import pandas as pd
# Dataframe.pivot_table
data = pd.read_table('../_Example_data.txt')
data_pivot = data.pivot_table(index='x', columns='y', values='MIDCounts', aggfunc='sum', fill_value=0)
print(data_pivot)
# groupby+unstack
data_unstack = data.groupby(['x', 'y']).agg({'MIDCounts':'sum'}).unstack().fillna(0)
print(data_unstack)
# csr_matrix
from scipy.sparse import csr_matrix
xDict = {c: i for i, c in enumerate(data['x'].sort_values().unique().tolist())}
yDict = {c: i for i, c in enumerate(data['y'].sort_values().unique().tolist())}
data['x_coo'] = data['x'].map(lambda x: xDict[x])
data['y_coo'] = data['y'].map(lambda x: yDict[x])
lasso_talbe = csr_matrix((data['MIDCounts'], (data['x_coo'], data['y_coo'])))
print(lasso_talbe)
