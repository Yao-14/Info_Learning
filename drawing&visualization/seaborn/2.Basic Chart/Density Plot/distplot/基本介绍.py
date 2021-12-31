'''
seaborn.distplot:集合了matplotlib的hist()与核函数估计kdeplot的功能,并增加了rugplot分布观测条显示与利用scipy库fit拟合参数分布的新颖用途。具体参数用法如下:
seaborn.distplot(a, bins=None, hist=True, kde=True, rug=False, fit=None, hist_kws=None, kde_kws=None, rug_kws=None, fit_kws=None, color=None, vertical=False, norm_hist=False, axlabel=None, label=None, ax=None)
a：Series、1维数组或者列表。观察数据。如果是具有name属性的Series对象，则该名称将用于标记数据轴。
bins：matplotlib hist()的参数，或None。可选参数。直方图bins（柱）的数目，若填None，则默认使用Freedman-Diaconis规则指定柱的数目。
hist：布尔值，可选参数。是否绘制（标准化）直方图。
kde：布尔值，可选参数。是否绘制高斯核密度估计图。
rug：布尔值，可选参数。是否在横轴上绘制观测值竖线。
fit：随机变量对象，可选参数。一个带有fit方法的对象，返回一个元组，该元组可以传递给pdf方法一个位置参数，该位置参数遵循一个值的网格用于评估pdf。
{hist, kde, rug, fit}_kws：字典，可选参数。
color：matplotlib color，可选参数。可以绘制除了拟合曲线之外所有内容的颜色。
vertical：布尔值，可选参数。如果为True，则观测值在y轴显示。
norm_hist：布尔值，可选参数。如果为True，则直方图的高度显示密度而不是计数。如果绘制KDE图或拟合密度，则默认为True。
axlabel：字符串，False或者None，可选参数。横轴的名称。如果为None，将尝试从a.name获取它；如果为False，则不设置标签。
label：字符串，可选参数。图形相关组成部分的图例标签。
ax：matplotlib axis，可选参数。若提供该参数，则在参数设定的轴上绘图。
'''