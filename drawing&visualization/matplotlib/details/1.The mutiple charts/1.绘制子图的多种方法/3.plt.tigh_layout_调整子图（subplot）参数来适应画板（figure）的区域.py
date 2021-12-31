'''
调整图层
tigh_layout自动调整子图（subplot）参数来适应画板（figure）的区域。它只会检查刻度标签（ticklabel），坐标轴标签（axis label），标题（title）。
轴（axes）包括子图（subplot）被画板（figure）的坐标指定。所以一些标签会超越画板（figure）的范围,因此通过plt.tight_layout()可以自动调整子图。
对于子图与子图之间的间隙调整，也可以使用plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
'''
import matplotlib.pyplot as plt
#绘制四个子图ax1和ax2
fig, ax = plt.subplots(2,2,figsize=(5,10), dpi=200)
ax1 = ax[0,0]
ax2 = ax[0,1]
ax3 = ax[1,1]
ax4 = ax[1,0]
#设置子图ax1的X轴标题和Y轴标题
ax1.set_xlabel(xlabel='Xzhou',labelpad=5,loc='center',fontsize=10,fontweight='bold',bbox=dict(boxstyle='Round',color='orangered'))
ax2.set_xlabel(xlabel='Xzhou',labelpad=5,loc='center',fontsize=10,fontweight='bold',bbox=dict(boxstyle='Round',color='orangered'))
ax3.set_xlabel(xlabel='Xzhou',labelpad=5,loc='center',fontsize=10,fontweight='bold',bbox=dict(boxstyle='Round',color='orangered'))
ax4.set_xlabel(xlabel='Xzhou',labelpad=5,loc='center',fontsize=10,fontweight='bold',bbox=dict(boxstyle='Round',color='orangered'))
ax1.set_title('sssss',fontsize=10,fontweight='bold',bbox=dict(boxstyle='Round',color='orangered'))
ax2.set_title('sssss',fontsize=10,fontweight='bold',bbox=dict(boxstyle='Round',color='orangered'))
ax3.set_title('sssss',fontsize=10,fontweight='bold',bbox=dict(boxstyle='Round',color='orangered'))
ax4.set_title('sssss',fontsize=10,fontweight='bold',bbox=dict(boxstyle='Round',color='orangered'))
plt.tight_layout()
plt.show()

