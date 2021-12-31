'''
Axes.set_xlabel(self, xlabel, fontdict=None, labelpad=None, *, loc=None, **kwargs)————设置X轴的标题
！主要参数：
xlabel：str，标题文本。
labelpad：float, default: rcParams["axes.labelpad"] (default: 4.0)，与坐标区边界框之间的点间距，包括刻度和刻度标签。如果没有，则前一个值保持原样。
loc：{'left', 'center', 'right'}, default: rcParams["xaxis.labellocation"] (default: 'center')，标签位置。
########################################################################################################################################

Axes.set_ylabel(self, xlabel, fontdict=None, labelpad=None, *, loc=None, **kwargs)————设置Y轴的标题
！主要参数：
ylabel：str，标题文本。
labelpad：float, default: rcParams["axes.labelpad"] (default: 4.0)，与坐标区边界框之间的点间距，包括刻度和刻度标签。如果没有，则前一个值保持原样。
loc：{'bottom', 'center', 'top'}, default: rcParams["yaxis.labellocation"] (default: 'center')，标签位置。

########################################################################################################################################
!其余一些常用通用参数：
fontfamily or family：{FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}
fontsize or size：float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
fontstretch or stretch：{a numeric value in range 0-1000, 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'}
fontstyle or style：{'normal', 'italic', 'oblique'}
fontvariant or variant：{'normal', 'small-caps'}
fontweight or weight：{a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}
rotation：float or {'vertical', 'horizontal'}
backgroundcolor：color，在不添加bbox时给标签添加一个长方形的背景色
bbox:给标题添加框————bbox=dict(boxstyle='',color='')
                        boxstyle包括：Circle	    circle	    pad=0.3
                                     DArrow	    darrow	    pad=0.3
                                     LArrow	    larrow	    pad=0.3
                                     RArrow	    rarrow	    pad=0.3
                                     Round	    round	    pad=0.3, rounding_size=None
                                     Round4	    round4	    pad=0.3, rounding_size=None
                                     Roundtooth	roundtooth	pad=0.3, tooth_size=None
                                     Sawtooth	sawtooth	pad=0.3, tooth_size=None
                                     Square 	square	    pad=0.3
'''

import matplotlib.pyplot as plt

#绘制两个子图ax1和ax2
fig, ax = plt.subplots(2,1,figsize=(5,10), dpi=200)
ax1 = ax[0]
ax1.bar(x=[1,2,3,4,5,6,7,8],height=[3,5,7,3,6,1,8,2])
#设置子图ax1的X轴标题和Y轴标题
ax1.set_xlabel(xlabel='Xzhou',labelpad=5,loc='center',fontsize=10,fontweight='bold',bbox=dict(boxstyle='Round',color='orangered'))
ax1.set_ylabel(ylabel='Yzhou',labelpad=5,loc='top',backgroundcolor='orangered')
plt.show()