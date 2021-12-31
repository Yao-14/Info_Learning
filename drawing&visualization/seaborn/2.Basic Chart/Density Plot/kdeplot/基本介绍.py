import matplotlib.pyplot as plt
import seaborn as sns

'''
核密度估计(kernel density estimation):是在概率论中用来估计未知的密度函数，属于非参数检验方法之一。通过核密度估计图可以比较直观的看出数据样本本身的分布特征。
seaborn.kdeplot:拟合并绘制单变量或双变量核密度估计图,具体参数用法如下:
seaborn.kdeplot(data, data2=None, shade=False, vertical=False, kernel='gau', bw='scott', gridsize=100, cut=3, clip=None, legend=True, cumulative=False, shade_lowest=True, cbar=False, cbar_ax=None, cbar_kws=None, ax=None, **kwargs)
data：一维阵列,输入数据
**data2：一维阵列，可选。第二输入数据。如果存在，将估计双变量KDE。
shade：布尔值，可选参数。如果为True，则在KDE曲线下方的区域中增加阴影（或者在数据为双变量时使用填充的轮廓绘制）。
vertical：布尔值，可选参数。如果为True，密度图将显示在x轴。
kernel：{‘gau’ | ‘cos’ | ‘biw’ | ‘epa’ | ‘tri’ | ‘triw’ }，可选参数。要拟合的核的形状代码，双变量KDE只能使用高斯核。
bw：{‘scott’ | ‘silverman’ | scalar | pair of scalars }，可选参数。用于确定双变量图的每个维的核大小、标量因子或标量的参考方法的名称。需要注意的是底层的计算库对此参数有不同的交互：statsmodels直接使用它，而scipy将其视为数据标准差的缩放因子。
gridsize：整型数据，可选参数。评估网格中的离散点数。
cut：标量，可选参数。绘制估计值以从极端数据点切割* bw。
clip：一对标量，可选参数。用于拟合KDE图的数据点的上下限值。可以为双变量图提供一对（上，下）边界。
legend：布尔值，可选参数。如果为True，为绘制的图像添加图例或者标记坐标轴。
cumulative：布尔值，可选参数。如果为True，则绘制kde估计图的累积分布。
shade_lowest：布尔值，可选参数。如果为True，则屏蔽双变量KDE图的最低轮廓。绘制单变量图或“shade = False”时无影响。当你想要在同一轴上绘制多个密度时，可将此参数设置为“False”。
cbar：布尔值，可选参数。如果为True并绘制双变量KDE图，为绘制的图像添加颜色条。
cbar_ax：matplotlib axes，可选参数。用于绘制颜色条的坐标轴，若为空，就在主轴绘制颜色条。
cbar_kws：字典，可选参数。
fig.colorbar（）的关键字参数。
ax：matplotlib axes，可选参数。要绘图的坐标轴，若为空，则使用当前轴。
kwargs：其他传递给plt.plot（）或plt.contour {f}的关键字参数，具体取决于是绘制单变量还是双变量图。

'''
