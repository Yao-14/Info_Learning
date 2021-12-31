import matplotlib.pyplot as plt
import seaborn as sns

listx = [1, 1, 1, 1, 2, 3, 2, 2, 2, 1, 3, 4, 5, 7, 1, 1, 3, 4, 6, 2]
sns.kdeplot(data=listx, shade=True, shade_lowest=True,color="gray", bw_adjust=1,cut=0,label='listx')
plt.legend()
plt.show()
'''
data:输入一维阵列数据
shade:如果为True，则在KDE曲线下方的区域中增加阴影;如果为Fales，则不添加阴影
shade_lowest:最外围颜色是否显示
color:设置曲线和阴影的颜色
bw_adjust:设置曲线的平滑程度(一般在0.5-1.5之间调节即可）
cut:设置曲线的绘制范围（比如一个list[1,1,1,2,3,4],如果cut=0则横坐标范围为1至4,如果cut=1则横坐标范围为0至5,如果cut=2则横坐标范围为-1至5,以此类推）
label:设置图例
'''
sns.kdeplot(listx, shade=True, color="gray", bw_adjust=1,vertical=True)
plt.show()
'''
vertical:如果为True，在纵轴上绘制密度分布。
'''
