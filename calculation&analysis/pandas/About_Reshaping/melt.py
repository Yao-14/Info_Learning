'''
pandas.melt(id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True)
    : 与pivot正好相反，生成逆透视表 (一般设置id_vars为index即可）
'''
import pandas as pd
# Dataframe.pivot_table
data = pd.read_table('../_Example_data.txt')
data_pivot = data.pivot_table(index='x', columns='y', values='MIDCounts', aggfunc='sum', fill_value=0)
data_pivot['X'] = data_pivot.index
print(data_pivot)
data_melt = pd.melt(data_pivot,id_vars='X', var_name='Y', value_name='Sum_counts')
print(data_melt)