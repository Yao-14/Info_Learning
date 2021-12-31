import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

raw_data1 = pd.read_excel('C4H4.xlsx')
# 删除不需要的数据
raw_data2 = raw_data1.copy()
raw_data2.drop(columns=['IF6', 'RT6', 'LY7', 'LE5', 'LY', 'LE'], inplace=True)
# 分别筛选出各组数据，并对每一组数据求平均值
raw_data3 = raw_data2.copy()
listjr = [i for i in raw_data3.columns if i.find('Jr') == 0]
listjc = [i for i in raw_data3.columns if i.find('Jc') == 0]
listjn = [i for i in raw_data3.columns if i.find('Jn') == 0]
raw_data3['Mean_jrs'] = np.mean(raw_data2.loc[:, listjr], axis=1)
raw_data3['Mean_jc'] = np.mean(raw_data2.loc[:, listjc], axis=1)
raw_data3['Mean_jn'] = np.mean(raw_data2.loc[:, listjn], axis=1)
# 通过每一组数据平均值的比较筛选基因ID
data_use1 = raw_data3[raw_data3['Mean_jrs'] - raw_data3['Mean_jc'] >= 50]
data_use2 = data_use1[data_use1['Mean_jn'] - data_use1['Mean_jc'] >= 50]
data_use2.index = range(len(data_use2.index))
data_use_raw = data_use2.drop(columns=['Mean_jrs', 'Mean_jc', 'Mean_jn'])

jrs = pd.DataFrame(['Jrs' for i in range(len(data_use_raw))])
jc = pd.DataFrame(['Jc' for i in range(len(data_use_raw))])
jn = pd.DataFrame(['Jn' for i in range(len(data_use_raw))])
start = pd.DataFrame([[0,0,0],[0,0,0]],columns=['ID','SP','EX'])

for i in data_use_raw.columns:
    if i.startswith('Jrs'):
        data = pd.concat([data_use_raw.iloc[:,0],jrs,data_use_raw.loc[:,[i]]],axis=1)
        data.columns =['ID','SP','EX']
        start = pd.concat([start,data],axis=0)
    elif i.startswith('Jc'):
        data = pd.concat([data_use_raw.iloc[:, 0], jc, data_use_raw.loc[:, [i]]], axis=1)
        data.columns = ['ID', 'SP', 'EX']
        start = pd.concat([start, data], axis=0)
    elif i.startswith('Jn'):
        data = pd.concat([data_use_raw.iloc[:, 0], jn, data_use_raw.loc[:, [i]]], axis=1)
        data.columns = ['ID', 'SP', 'EX']
        start = pd.concat([start, data], axis=0)

start.drop(index=[0,1],inplace=True)
print(start)


fig = plt.figure(figsize=[20, 30], dpi=100)
sns.set_theme(style="ticks")
sns.boxplot(x='ID',y='EX',hue='SP',data=start, palette='Set1')
sns.swarmplot(x='ID',y='EX',hue='SP',data=start, palette='Set1')
plt.savefig('Example1.pdf')
#boxplot(data_use_raw)