import matplotlib.pyplot as plt
import seaborn as sns

list1 = [1, 1, 1, 1, 2, 3, 2, 2, 2, 1, 3, 4, 5, 7, 1, 1, 3, 4, 6, 2]
list2 = [3, 2, 4, 8, 6, 1, 3, 5, 1, 0, 6, 2, 9, 6, 4,1,2,7,3,2]
#颜色设置——调色盘
cmap = sns.color_palette(palette='Greens',as_cmap =True)
#绘制双变量数据密度分布图————双变量无法展示观测条，需要另行绘制
sns.kdeplot(x=list1,y=list2,cbar = True,shade = True,cmap = cmap,shade_lowest = False,n_levels = 10)
#绘制x轴上的观测条
sns.rugplot(x=list1,height=0.05 ,color = 'g', alpha = 0.5)
#绘制x轴上的观测条
sns.rugplot(y=list2,height=0.05 ,color = 'r', alpha = 0.5)
plt.show()
'''
x:输入第一组一维阵列数据
y:输入第二组一维阵列数据
shade:如果为True，则在KDE曲线下方的区域中增加阴影;如果为Fales，则不添加阴影
shade_lowest:最外围颜色是否显示
cmap:设置颜色
cbar:如果为True则为绘制的图像添加颜色条图例;如果为Fales，则不添加颜色条图例
bw_adjust:设置曲线的平滑程度(一般在0.5-1.5之间调节即可）
cut:设置曲线的绘制范围（比如一个list[1,1,1,2,3,4],如果cut=0则横坐标范围为1至4,如果cut=1则横坐标范围为0至5,如果cut=2则横坐标范围为-1至5,以此类推）
n_levels:曲线个数(如果非常多，则会越平滑)
'''