import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('示例文件.xlsx',index_col=0)
print(data)
sns.set_theme()
#设置颜色条图例的大小
grid_kws = {"height_ratios": (.9, .01), "hspace": .3}
f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws,figsize=(20, 40))

sns.heatmap(data, ax=ax,cmap="YlGnBu",fmt ='.2f',
            annot=True,annot_kws={'size':15,'weight':'bold', 'color':'black'},
            linewidths=1.5,linecolor='white',square=True,mask=data<100,
            cbar_ax=cbar_ax,cbar_kws={"orientation": "horizontal"})
'''
fontsize：标签字体大小，取整数
verticalalignment：表示垂直对齐方式 ，可选'center'，'top'，'bottom'，'baseline'等
horizontalalignment：表示水平对齐方式 ，可以填'center'，'right'，'left'等
rotation：表示标签的旋转角度，以逆时针计算，取整
family： 用来设置字体，如：'Times New Roman'
style： 设置字体的风格，如：'italic'
weight： 字体的粗细, 如：'light'
bbox： 给字体添加框,如 bbox=dict(facecolor='red', alpha=0.5)
'''
#设置横坐标
ax.set_xticklabels([i for i in data.columns],fontsize=20,weight='bold',color='black',rotation =30)
#设置纵坐标
ax.set_yticklabels([i for i in data.index],fontsize=20,weight='bold',color='black')
plt.savefig('Heatmap Example.pdf')