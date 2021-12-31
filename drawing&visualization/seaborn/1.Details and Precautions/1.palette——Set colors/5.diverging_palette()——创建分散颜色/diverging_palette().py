import matplotlib.pyplot as plt
import seaborn as sns

sns.palplot(sns.diverging_palette(h_neg=240,h_pos=10, s=85, l=65, n=8, center='light',as_cmap =False))
'''
h_neg：起始颜色值,值区间0-359
h_pos：终止颜色值，值区间0-359
s：饱和度，值区间0-100
l：亮度，值区间0-100
n：调色板中的颜色数（如果为not，返回一个colormap）
center：调色板中心为亮或暗——{'light', 'dark'}, 默认为light
as_cmap：默认为False，返回颜色列表。如果为True值，则返回matplotlib colormap而不是颜色列表。
'''
plt.show()
