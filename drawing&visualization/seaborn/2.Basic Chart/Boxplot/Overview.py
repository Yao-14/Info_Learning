'''
seaborn.boxplot(*, x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None, color=None, palette=None,
                saturation=0.75, width=0.8, dodge=True, fliersize=5, linewidth=None, whis=1.5, ax=None, **kwargs)
x, y, hue.:数据集中用于绘图的三个变量名称
data.:用于绘图的数据集
order, hue_order：可以从用于绘制的变量中筛出需要绘制的特例。
                 如x这一列数据中包含['gene1','gene2','gene3'],但是我只想画['gene1','gene2']，则用order=['gene1','gene2']筛选出来。
orient:'v' or 'h'.图的方向垂直或水平.
color:颜色，或者用palette调色板
palette：同上
saturation
width
dodge:True or False.若为True，则将箱线图分列绘制，若为False则在同一列上绘制————详细差别看Example2
fliersize
linewidth
whis
ax
'''


#Example
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_theme(style="ticks")

data = pd.DataFrame([['gene1','day1','sp1',20],['gene1','day1','sp2',23],['gene1','day1','sp3',21],['gene1','day1','sp4',29],
                     ['gene1','day2','sp1',27],['gene1','day2','sp1',12],['gene1','day2','sp3',16],['gene1','day2','sp4',22],
                     ['gene1','day3','sp1',31],['gene1','day3','sp2',32],['gene1','day3','sp3',28],['gene1','day3','sp4',26],
                     ['gene2','day1','sp1',20],['gene2','day1','sp2',23],['gene2','day1','sp3',21],['gene2','day1','sp4',29],
                     ['gene2','day2','sp1',27],['gene2','day2','sp1',12],['gene2','day2','sp3',16],['gene2','day2','sp4',22],
                     ['gene2','day3','sp1',31],['gene2','day3','sp2',32],['gene2','day3','sp3',28],['gene2','day3','sp4',26],
                     ['gene3','day1','sp1',20],['gene3','day1','sp2',23],['gene3','day1','sp3',21],['gene3','day1','sp4',29],
                     ['gene3','day2','sp1',27],['gene3','day2','sp1',12],['gene3','day2','sp3',16],['gene3','day2','sp4',22],
                     ['gene3','day3','sp1',31],['gene3','day3','sp2',32],['gene3','day3','sp3',28],['gene3','day3','sp4',26]],
                     columns=['Gene','Day','Species','Expression'])
test1 = sns.boxplot(x="Gene", y="Expression", hue="Species", data=data)
plt.savefig('test1.pdf')
