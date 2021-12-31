import matplotlib.pyplot as plt
import seaborn as sns

sns.palplot(sns.hls_palette(n_colors =20 , l = 0.6, s =0.7,as_cmap=False))
'''
n_colors：从调色盘中挑选的颜色色块个数（如n_colors =8指选择8个颜色色块）
l：设定亮度，范围0 - 1。（如l = 0.6指设定亮度为0.6）
s：设定饱和度，范围0 - 1。（如s =0.7指设定饱和度为0.7）
不同的亮度和饱和度搭配可以展示出不同的颜色色盘
as_cmap：默认为False，返回颜色列表。如果为True值，则返回matplotlib colormap而不是颜色列表。
'''
plt.show()


