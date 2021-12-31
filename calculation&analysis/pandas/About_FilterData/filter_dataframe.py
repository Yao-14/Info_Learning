import pandas as pd

data = pd.DataFrame([['b',2,3,4,5],
                     ['a','b','c','d','e'],
                     ['aa', None,'cc','dd','ee']])

# .map(lambda) 筛选数据
print(data[data[0].map(lambda x:x == 'a')])


# .where(cond, inplace, other) where接受Bool类型的值，若为False将被赋予默认的NaN或者other指定的值
cond = data[2] == 'c';cond2 = data[3] == 'd'
data[2].where(cond, inplace=True,other='c++'); print(data)
data[4].where(cond & cond2, inplace=True, other='bufuhe'); print(data)
# .mask() 与where恰好相反，接受Bool类型的值，若为True将被赋予默认的NaN或者other指定的值
data[3].mask(cond2,inplace=True,other='d--'); print(data)


# .str.contains() 筛选字符串中包含某些内容中的数据（注意该列必须全部都是字符串数据，可以添加 | 代表或者）
print(data[data[0].str.contains('a|b')])


# .isin() 筛选属于某个列表中的数据
ex_list = ['c','cc','d']
print(data[data[2].isin(ex_list)])    # 正选操作
print(data[~data[2].isin(ex_list)])   # 添加 ~ 进行反选操作


# .any(axis) 如果至少有一个值为True，则返回True
print(data.isnull().any(axis=1))
# .all(axis) 如果所有值为True，则返回True
print(data.isnull().all(axis=1))