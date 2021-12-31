from dfply import *
import pandas as pd
data = pd.read_excel('example_file.xlsx',header=None)
data.columns=['Chr','Start','End']

#rename（new_name = old_name)————函数会将新列名覆盖原列名。老名字可以有两种输入方法，一种是X.Chr或者是'Chr'
df1 = data >> rename(chr=X.Chr, start='Start')
print(df1)
