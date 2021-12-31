import matplotlib.pyplot as plt
import seaborn as sns
listx = [1, 1, 1, 1, 2, 3, 2, 2, 2, 1, 3, 4, 5, 7, 1, 1, 3, 4, 6, 2]
ax1 = sns.distplot(a=listx,rug=True,kde=True,hist=True,bins = 10,vertical=False,color='green',axlabel='xlabel',norm_hist=True)
'''
a：Series、1维数组或者列表。观察数据。如果是具有name属性的Series对象，则该名称将用于标记数据轴。
hist：布尔值，可选参数。是否绘制（标准化）直方图。
kde：布尔值，可选参数。是否绘制高斯核密度估计图。
rug：布尔值，可选参数。是否在横轴上绘制分布观测条。
bins：直方图bins（柱）的数目。
vertical：布尔值，可选参数。如果为True，则观测值在y轴显示。
color：matplotlib color，可选参数。可以绘制除了拟合曲线之外所有内容的颜色。
axlabel：字符串，False或者None，可选参数。横轴的名称。如果为None，将尝试从a.name获取它；如果为False，则不设置标签。
norm_hist：布尔值，可选参数。如果为True，则直方图的高度显示密度而不是计数。如果绘制KDE图或拟合密度，则默认为True。
'''
plt.show()

#直方图、高斯核密度估计图和分布观测条各个参数分开设置——hist_kws、kde_kws、rug_kws
ax2 = sns.distplot(a=listx,rug=True,kde=True,hist=True,bins = 5,
                   rug_kws={"color": "b","alpha": 0.6,'height':0.05,'label':'rug'},
                   kde_kws={"color": "k", "linewidth": 3,"linestyle":"--","alpha": 0.6,"label": "KDE"},
                   hist_kws={"histtype": "stepfilled", "linewidth": 3,"alpha": 0.6, "color": "g","label":'Hist'},
                   vertical=False,color='green',axlabel='xlabel',norm_hist=True)
'''
rug_kws={"color": "b",'height':0.05,label = 'rug'}
#"color":设定颜色
#"alpha":设定线条透明度
#'height':设定高度
#"label":设定图例标签名

kde_kws={"color": "k", "linewidth": 3,'linestyle':'--',"alpha": 0.6, "label": "KDE"}
#"color":设定颜色
#'linewidth':设定线条宽度
#'linestyle':设定线条的风格,风格包括'-','--','-.',':','None',']'
#"alpha":设定线条透明度
#"label":设定图例标签名

hist_kws={"histtype": "stepfilled", "color": "g", "linewidth": 3,"alpha": 0.6,"label":'Hist'}
#"histtype":设定直方图的风格,风格包括：'bar'、'barstacked'、'step'、'stepfilled'
#"color":设定颜色
#'linewidth':设定线条宽度
#"alpha":设定线条透明度
#"label":设定图例标签名
'''
plt.legend()
plt.show()
