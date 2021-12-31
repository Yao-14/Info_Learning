'''
grid()函数用于设置绘图区网格线。
matplotlib.pyplot.grid(b=None, which='major', axis='both', **kwargs)。
grid()的参数如下：
b：是否显示网格线，布尔值或None。如果没有关键字参数，则b为True，如果b为None且没有关键字参数，相当于切换网格线的可见性。
which：网格线显示的尺度，取值范围为{'major', 'minor', 'both'}，默认为'major'。'major'为主刻度、'minor'为次刻度。
axis：选择网格线显示的轴，取值范围为{'both', 'x', 'y'}，默认为'both'。
color/c : 设置网格线的颜色。
linestyle/ls :设置网格线的风格。———— '-','--','-.',':','None',']'
linewidth/lw : 设置网格线的宽度。

'''
import matplotlib.pyplot as plt
plt.grid()
plt.show()