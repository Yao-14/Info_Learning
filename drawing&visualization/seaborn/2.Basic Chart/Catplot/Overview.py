'''
seaborn.catplot(*, x=None, y=None, hue=None, data=None, row=None, col=None, col_wrap=None,
                estimator=<function mean at 0x7fecadf1cee0>, ci=95, n_boot=1000, units=None, seed=None, order=None,
                hue_order=None,row_order=None, col_order=None, kind='strip', height=5, aspect=1, orient=None, color=None,
                palette=None, legend=True, legend_out=True, sharex=True, sharey=True, margin_titles=False, facet_kws=None, **kwargs)¶

简介:catplot用于在 FacetGrid 上绘制分类图的图形级界面。此函数提供对多个轴级函数的访问，这些函数使用多种视觉表示形式之一显示数值与一个或多个分类变量之间的
    关系。 该参数选择要使用的底层轴级函数：kind
Categorical scatterplots(分类散点图):
    kind="strip": stripplot() (the default)
    kind="swarm": swarmplot()
Categorical distribution plots(分类分布图):
    kind="box": boxplot()
    kind="violin": violinplot()
    kind="boxen": boxenplot()
Categorical estimate plots(分类估计图):
    kind="point": pointplot()
    kind="bar": barplot()
    kind="count": countplot()

Parameters
x, y, hue.:数据集中用于绘图的三个变量名称
data.:用于绘图的数据集
row, col.:通过一个变量作为变量分类绘制多个分类图。
col_wrap.:设置每一行最多有多少列
estimator.:
ci.:围绕估计值绘制的置信区间的大小.如果为“sd”,则跳过引导并绘制观测值的标准偏差.如果无则不执行,也不会绘制误差线.
n_boot.:计算置信区间时使用的引导迭代次数。
units.:
seed.:
order, hue_order.:
row_order, col_order.:
kind.:要绘制的绘图类型对应于分类轴级别绘图函数的名称.选项包括：“strip”、“swarm”、“box”、“violin”、“boxen”、“point”、“bar”或“count”.
height.:每个刻面的高度（以英寸为单位）.
aspect.:每个面的纵横比.因此以英寸为单位给出每个面的宽度:aspect * height.
orient.:'v' or 'h'.图的方向垂直或水平.
color.:
palettepalette.:
legend.:True or False.是否绘制图例.
legend_out.:True or False. If the figure size will be extended, and the legend will be drawn outside the plot on the center right.True
sharex,sharey.:True or False.是否共用相同的x轴标签或y轴标签.

详情请看：
https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot
'''

#Example
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
plt.figure(figsize=[30,60])
sns.set_theme(style="ticks")
data = pd.DataFrame([['CHR1','AAA',2,3],['CHR2','BBB',12,13],
                     ['CHR3','CCC',21,3],['CHR1','CCC',9,6],
                     ['CHR2','AAA',20,8],['CHR3','AAA',12,3],
                     ['CHR1','BBB',2,12],['CHR2','AAA',2,8]],
                     columns=['Chr','Type','Start','End'])
g = sns.catplot(x="Start", y="End", hue="Type", data=data,kind='strip',
                col='Chr',col_wrap=3,height=10,aspect=0.7,orient='h',
                legend=True,legend_out=True,sharex=False)
plt.show()