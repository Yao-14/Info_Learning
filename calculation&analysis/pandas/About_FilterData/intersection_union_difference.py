"""
获取两个 DataFrame 的交集、并集、差集，可用于筛选数据（比 .isin(list)更加高效，可以适用于同时在多列中的筛选）

该方法使用 pd.merge() 实现
"""