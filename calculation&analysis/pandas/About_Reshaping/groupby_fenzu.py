
'''

一.进行分组操作的过程可以概括为：split-apply-combine三步：
    1.按照分组键将数据分组. (分组键可以是数组, 列表, 字典, Series, 函数, 默认axis=0按行分组，可指定axis=1对列分组。)
    2.对于每组应用函数, 可以是python自带函数, 可以是我们自己编写的函数.(option)
    3.将函数计算后的结果聚合.

'''


import pandas as pd
import numpy as np
df = pd.DataFrame(
    [
        ['yaojiajun', 22, 'student', 'shenzheng', 'male'],
        ['huangjinghua', 20, 'student', 'xian', 'female'],
        ['cuixinrui', 21, 'student', 'shenzheng', 'male'],
        ['sunrui', 21, 'student', 'xian', 'male'],
        ['liude', 21, 'student', 'shenzheng', 'male'],
        ['guojiahui', 26, 'teacher', 'xian', 'female'],
    ],
    columns=['Name', 'Age', 'Identity', 'Live', 'Gender'],
)

df2 = pd.DataFrame(np.random.randint(0, 10, size=(5, 7)),
     columns=['gene1', 'gene2', 'gene3', 'gene4', 'gene5', 'gene6', 'gene7'],
     index=['cell1', 'cell2', 'cell3', 'cell4', 'cell5'])

print('\n分组基础操作1：基于一列进行分组并迭代获取每一组信息****************************************************************')
# 分组基础操作1：基于一列进行分组并迭代获取每一组信息
df_test1 = df.groupby('Live')
for name, group in df_test1:
    print(name, group)

print('\n分组基础操作2：基于多列进行分组并迭代获取每一组信息****************************************************************')
# 分组基础操作2：基于多列进行分组并迭代获取每一组信息
df_test2 = df.groupby(['Live','Identity'])
for (name1, name2), group in df_test2:
    print(name1, name2, '\n', group)

print('\n分组基础操作3/4/5：通过dict或Series对列进行聚合分组(在纯数值Dataframe中使用效果极佳)*********************************')
# 分组基础操作3：通过字典对列进行聚合
mapping = {'gene1': 'tissue1', 'gene2': 'tissue2','gene3': 'tissue2', 'gene4': 'tissue1',
           'gene5': 'tissue2', 'gene6': 'tissue1', 'gene7': 'tissue2'}
df2_test1 = df2.groupby(mapping, axis=1)
for name, group in df2_test1:
    print(name, '\n', group)
# 分组基础操作4：通过Series对列进行聚合
mapping_series = pd.Series(mapping)
df2_test2 = df2.groupby(mapping_series, axis=1)
for name, group in df2_test2:
    print(name, '\n', group)
# 分组基础操作5：对列进行聚合并进行数值计算
df2_test3 = df2.groupby(mapping, axis=1).sum()
print(df2_test3)
