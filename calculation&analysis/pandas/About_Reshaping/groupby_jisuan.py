
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 10, size=(5, 7)),
     columns=['gene1', 'gene2', 'gene3', 'gene4', 'gene5', 'gene6', 'gene7'],
     index=['cell1', 'cell2', 'cell3', 'cell4', 'cell5'])

print('\n计算操作1：describe()描述组内数据的基本统计量, '
      '包括每个分组中的数量(count), 平均值(mean), 标准差(std), 最小值(min), 25%值(25%), 50%值(50%)和75%值(75%)')
# 计算操作1-1：describe()描述组内数据的基本统计量, 获取所有分组中所有列数据情况
print(df.groupby('gene1').describe())
# 计算操作1-2：describe()描述组内数据的基本统计量, 获取所有分组中gene2列数据情况
print(df.groupby('gene1')['gene2'].describe())

print('\n计算操作2：计算函数****************************************************************')
# 计算操作2-1：mean()组内均值计算
print(df.groupby('gene1').mean())
# 计算操作2-2：sum()组内均值计算
print(df.groupby('gene1').sum())
# 计算操作2-3：count()组内个数计算
print(df.groupby('gene1').count())

print('\n计算操作2：agg()进行numpy中的运算****************************************************************')
# 计算操作3：agg()进行numpy中的运算
print(df.groupby('gene1').agg(np.mean))