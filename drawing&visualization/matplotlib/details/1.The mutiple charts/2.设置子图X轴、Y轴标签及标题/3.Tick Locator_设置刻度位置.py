
'''
Python-matplotlib「刻度(ticker)」 的使用方法之Tick locators 刻度位置介绍

Tick Locator————Tick Locator主要设置刻度位置，其中Locator的子类主要如下：
定位器	                解释说明
AutoLocator	            自动定位器,多数绘图的默认刻度线定位。
MaxNLocator	            在最合适的位置找到带有刻度的最大间隔数。
LinearLocator	        从最小到最大之间的均匀刻度定位。
LogLocator	            从最小到最大呈对数形式的刻度定位。
MultipleLocator	        刻度和范围是基数的倍数；整数或浮点数。(自定义刻度用较多的方法)。
FixedLocator	        固定刻度定位。刻度位置是固定的。
IndexLocator	        索引定位器。
NullLocator	            空定位器。无刻度位置。
SymmetricalLogLocator	与符号规范一起使用的定位器；对于超出阈值的部分，其工作原理类似于LogLocator，如果在限制范围内，则将其加0。
LogitLocator	        用于logit缩放的刻度定位器。
OldAutoLocator	        选择一个MultipleLocator并动态重新分配它，以在导航期间进行智能打勾。(直接翻译，感觉用的不多)。
AutoMinorLocator	    轴为线性且主刻度线等距分布时，副刻度线定位器。将主要刻度间隔细分为指定数量的次要间隔，根据主要间隔默认为4或5。
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.rcParams['font.family'] = "Times New Roman"


def setup(ax, title):
    """Set up common parameters for the Axes in the example."""
    # only show the bottom spine
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')


fig, axs = plt.subplots(8, 1, figsize=(8, 6), dpi=200)

# Null Locator
setup(axs[0], title="NullLocator()")
axs[0].xaxis.set_major_locator(ticker.NullLocator())
axs[0].xaxis.set_minor_locator(ticker.NullLocator())

# Multiple Locator
setup(axs[1], title="MultipleLocator(0.5)")
axs[1].xaxis.set_major_locator(ticker.MultipleLocator(0.5))
axs[1].xaxis.set_minor_locator(ticker.MultipleLocator(0.1))

# Fixed Locator
setup(axs[2], title="FixedLocator([0, 1, 5])")
axs[2].xaxis.set_major_locator(ticker.FixedLocator([0, 1, 5]))
axs[2].xaxis.set_minor_locator(ticker.FixedLocator(np.linspace(0.2, 0.8, 4)))

# Linear Locator
setup(axs[3], title="LinearLocator(numticks=3)")
axs[3].xaxis.set_major_locator(ticker.LinearLocator(3))
axs[3].xaxis.set_minor_locator(ticker.LinearLocator(31))

# Index Locator
setup(axs[4], title="IndexLocator(base=0.5, offset=0.25)")
axs[4].plot(range(0, 5), [0] * 5, color='white')
axs[4].xaxis.set_major_locator(ticker.IndexLocator(base=0.5, offset=0.25))

# Auto Locator
setup(axs[5], title="AutoLocator()")
axs[5].xaxis.set_major_locator(ticker.AutoLocator())
axs[5].xaxis.set_minor_locator(ticker.AutoMinorLocator())

# MaxN Locator
setup(axs[6], title="MaxNLocator(n=4)")
axs[6].xaxis.set_major_locator(ticker.MaxNLocator(4))
axs[6].xaxis.set_minor_locator(ticker.MaxNLocator(40))

# Log Locator
setup(axs[7], title="LogLocator(base=10, numticks=15)")
axs[7].set_xlim(10 ** 3, 10 ** 10)
axs[7].set_xscale('log')
axs[7].xaxis.set_major_locator(ticker.LogLocator(base=10, numticks=15))

plt.tight_layout()
plt.show()