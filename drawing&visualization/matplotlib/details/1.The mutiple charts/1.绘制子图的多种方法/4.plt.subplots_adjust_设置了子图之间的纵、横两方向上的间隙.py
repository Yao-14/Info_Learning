'''
plt.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=0.15,hspace=0.15)————一般不与plt.tight_layout()共同出现

left  # the left side of the subplots of the figure
right  # the right side of the subplots of the figure
bottom  # the bottom of the subplots of the figure
top  # the top of the subplots of the figure
wspace # the amount of width reserved for blank space between subplots,expressed as a fraction of the average axis width
hspace # the amount of height reserved for white space between subplots, expressed as a fraction of the average axis height
通过wspace和hspace设置子图之间的间隙，
通过left、bottom、right、top设置子图与画板的间隙
'''
import matplotlib.pyplot as plt
#绘制四个子图ax1和ax2
fig, ax = plt.subplots(2,2,figsize=(10,10), dpi=200)
plt.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=0.5,hspace=0.5)
ax1 = ax[0,0]
ax2 = ax[0,1]
ax3 = ax[1,1]
ax4 = ax[1,0]

plt.show()
