'''
在同一张图上绘制多个y轴的本质就是绘制多个子图，但所有的子图共用一个x轴

绘制多个y轴的关键函数是：host = host_subplot(111)
                      par = host.twinx()
即同时绘制host这个子图和par这个子图，而后分别在这两个子图中绘图，得到两个y轴。
'''

#绘制三y轴图
from mpl_toolkits.axes_grid1 import host_subplot
from mpl_toolkits import axisartist
import matplotlib.pyplot as plt

#关键步骤，绘制三个子图
host = host_subplot(111)
par1 = host.twinx()
par2 = host.twinx()
par2.axis["right"] = par2.new_fixed_axis(loc="right", offset=(60, 0))
#绘制host图（以左侧y轴为轴）
p1 = host.plot([0, 1, 2], [0, 1, 2], label="Y左")
#绘制par1图（以右侧第一根y轴为轴）
p2 = par1.plot([0, 1, 2], [0, 3, 2], label="Y右1")
#绘制par2图（以右侧第二根y轴为轴）
p3 = par2.plot([0, 1, 2], [1, 7, 4], label="Y右2")

#设置每一条轴的label及其颜色
host.set_xlabel("X轴")
host.set_ylabel("Y左")
par1.set_ylabel("Y右1")
par2.set_ylabel("Y右2")

host.yaxis.get_label().set_color('green')
par1.yaxis.get_label().set_color('red')
par2.yaxis.get_label().set_color('blue')

plt.show()