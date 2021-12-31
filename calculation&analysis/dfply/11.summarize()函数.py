'''
summarize可以接受任意数量的关键字参数，这些参数将返回标有键的新列，这些键是原始DataFrame中列的汇总函数。
summarize主要是通过使用numpy中的数学函数来进行计算
np.sum(a)  # 求和
np.sum(a, axis=0, dtype=None)  # 按列求和，dtype：指定返回数组类型
np.sum(a, axis=1)  # 按行求和
np.prod(a, axis=1)  # 按行乘积
np.nanprod(a, axis=None, dtype=None)  # a可以带nan值
np.min(a, axis=None)  # 求最小值，axis指定行列，同理有np.nanmin(),
np.max(a, axis=None)  # 求最大值，axis指定行列，同理有np.nanmax()
np.cumsum(a, axis=None)  # 累积和统计，axis指定行列，np.nancumsum()
np.cumprod(a, axis=None)  # 累积乘积统计，axis指定行列，np.nancumprod(a, axis=None)
np.mean(a, axis=None, dtype=None)  # 平均值统计，np.nanmean(a, axis=None, dtype=None)
np.average(a, axis=None, weights=None, returned=False) # 加权平均值统计，axis指定行列，weights指定每一行列的权重(数组)，returned：False返回数组，True返回元组
np.median(a, axis=None)  # 中值统计，np.nanmedian(a, axis=None)
np.var(a, axis=None, dtype=None)  # 方差计算
np.std(a, axis=None, dtype=None)  # 标准差计算
np.ptp(a, axis=None)  # 轴最大最小值差值计算

'''
from dfply import *
import pandas as pd
data = pd.read_excel('example_file.xlsx',header=None)
data.columns=['Chr','Start','End']
#1.summarize(Size_mean=X.Size.mean(),Size_std=X.Size.std())：很简单求得Size列的平均值与标准差
df1 = data >> mutate(Size=X.End-X.Start) >> summarize(Size_mean=X.Size.mean(),Size_std=X.Size.std())
print(df1)

#2.搭配group_by函数求得Chr列每一类的各自的平均值与标准差
df2 = (data >>
       mutate(Size=X.End-X.Start) >>
       group_by(X.Chr) >>
       summarize(Size_mean=X.Size.mean(),Size_std=X.Size.std()))
print(df2)

#3.summarize_each(function_list, *columns):效果同上，这个直接应用numpy模块中的函数,可同时计算多列数据
df3 = (data >>
       mutate(Size=X.End-X.Start) >>
       group_by(X.Chr) >>
       summarize_each([np.mean,np.std], X.Size,X.Start))
print(df3)