import matplotlib.pyplot as plt
import seaborn as sns
'''
深色调色盘以输入的颜色为最浅的颜色，而后向黑色方向变化设置调色盘
深色调色盘以输入的颜色为最深的颜色，而后向白色方向变化设置调色盘
参数：
color：高值的基色，输入格式为十六进制、RGB 元组或者颜色名字。
n_colors：调色板中的颜色数。
reverse：默认为False，调色板将从亮到暗。如果为True值，则调色板将从暗到亮。
as_cmap：默认为False。如果为 True 值，则返回matplotlib colormap而不是列表。
'''
#深色调色盘
sns.palplot(sns.dark_palette(color='blue',n_colors=6 ,reverse=False))  # 按照blue做深色调色盘
plt.show()
#浅色调色盘
sns.palplot(sns.light_palette(color='green')[1:])  # 按照green做浅色调色盘
plt.show()

