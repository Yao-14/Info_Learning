'''
separate（column，into，sep =“[\ W _] +”，remove = True，convert = False，extra ='drop'，fill ='right'）函数将列拆分为多个列。
separate（）有各种各样的参数：
         column：要拆分的列。
         into：新列的名称。
         sep：可以根据字符串或整数位置以拆分列。
         remove：指示是否删除原始列。
         convert：指示是否应将新列转换为适当的类型。
         extra：指示对多余列的处理。可以选择丢弃('drop')，或者合并给最后一列('merge')。
         fill：可以是'right'在最右边的列中填充np.nan值来填充缺失的部分，可以是'left'在最左边的列中填充np.nan值来填充缺失的部分
'''
from dfply import *
import pandas as pd
data = pd.read_excel('example_file.xlsx',header=None)
data.columns=['Chr','Start','End']
df1 = data >> separate(X.Chr, ['chr', 'number'],sep='r' ,remove=False, convert=True,extra='merge', fill='right')
print(df1)