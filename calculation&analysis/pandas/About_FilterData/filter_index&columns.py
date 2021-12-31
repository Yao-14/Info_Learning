import pandas as pd
data = pd.DataFrame([[1,2,3,4,5],
                     ['a','b','c','d','e'],
                     ['aa','bb','cc','dd','ee']])
data.columns = ['first','second','third','forth','fifth']

# .filter 筛选特定的行或者列.( items: 固定列名; regex: 正则表达式; like: 模糊查询; axis: 控制行或列 )

# 筛选列名为'first','fifth'的列
print(data.filter(items=['first','fifth'],axis=1))
print(data.filter(items=[0,2],axis=0))

# 筛选包括字母fo的列
print(data.filter(regex='fo',axis=1))

# 筛选索引中有2的行
print(data.filter(like='2', axis=0))

# 多个filter共用
print(data.filter(regex='fi',axis=1).filter(like='2', axis=0))