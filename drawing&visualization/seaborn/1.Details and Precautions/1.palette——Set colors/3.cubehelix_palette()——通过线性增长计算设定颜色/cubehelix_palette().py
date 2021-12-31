import matplotlib.pyplot as plt
import seaborn as sns
#用 cubehelix 系统制作顺序调色板,生成亮度呈线性减小(或增大)的 colormap。
sns.palplot(sns.cubehelix_palette(n_colors=6, start=0, rot=0.4, gamma=1.0, hue=0.8,
                                  light=0.9, dark=0.1, reverse=False, as_cmap=False))
'''
n_colors：调色板中的颜色数。
start：第一个色调，范围0-3
rot：围绕调色板范围内的色相控制盘旋转。
gamma：Gamma系数，数值越大颜色越暗，范围大于0
hue：颜色的饱和度，范围0-1
dark：调色板中最暗颜色的强度，范围0-1（将dark值调高就可以将最深的颜色变浅一点）
light：调色板中最浅颜色的强度，范围0-1（将light值调低就可以将最浅的颜色变深一点）
reverse：默认为False，调色板将从亮到暗。如果为 True 值，则调色板将从暗到亮。
as_cmap：默认为False，返回颜色列表。如果为True值，则返回matplotlib colormap而不是颜色列表。
'''
plt.show()