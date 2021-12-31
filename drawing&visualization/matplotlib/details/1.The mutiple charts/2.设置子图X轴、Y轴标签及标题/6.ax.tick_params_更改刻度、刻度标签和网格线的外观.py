'''
Axes.tick_params(self,axis='both', **kwargs)————更改刻度、刻度标签和网格线的外观。

！必需参数:
axis：{'x', 'y', 'both'}, default: 'both',应用参数的轴。
which：{'major', 'minor', 'both'}, default: 'major',应用参数的刻度组。
reset：bool, default: False,是否在更新之前将刻度重置为默认值。

！可选参数:（以下刻度就是指那根线）
direction：{'in', 'out', 'inout'},在轴内、轴外或两者之间放置刻度。
length：float,刻度长度。
width：float,刻度宽度。
color：color,刻度颜色。
pad：float,刻度和标签之间的距离。
labelsize：float or str,标签字体大小。
labelcolor：color,标签字体颜色。
colors：color,刻度颜色和标签颜色。
zorder：float,
bottom, top, left, right：bool,是否绘制相应的刻度。
labelbottom, labeltop, labelleft, labelright：bool，是否绘制相应的刻度标签。
labelrotation：float，刻度标签旋转
grid_color：color，网格线颜色。
grid_alpha：float，网格线的透明度：0（透明）到 1（不透明）。
grid_linewidth：float，网格线的宽度。
grid_linestyle：str，网格线的样式，{'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
'''

import matplotlib.pyplot as plt
from matplotlib import ticker

fig, ax = plt.subplots(2,1,figsize=(5,5), dpi=200)
ax1 = ax[0]
ax1.bar(x=[1,2,3,4,5,6,7,8],height=[3,5,7,3,6,1,8,2])
ax1.set_xticks([1,2,3,4,5,6,7,8])
ax1.set_xticklabels(['A','B','C','D','E','F','G','H'])
#设置刻度、刻度标签和网格线的外观
ax1.tick_params(axis='x', labelrotation=15, labelsize=10, length=5, pad=5)
ax1.tick_params(axis='y', labelsize=9, length=3, direction='inout')

plt.show()