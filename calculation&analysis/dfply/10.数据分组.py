#DataFrames使用group _ by ( )函数沿变量分组。
# ungroup ( )函数不分组，对DataFrame进行分组后链接起来的函数被分组应用，直到返回或解分组。分层/多索引自动删除。
from dfply import *
import pandas as pd
data = pd.read_excel('example_file.xlsx',header=None)
data.columns=['Chr','Start','End']
print(data >> group_by(X.Chr))