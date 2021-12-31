'''
直接使用ax.set_xticks()和ax.set_xticklabels()命名刻度标签，
'''

import matplotlib.pyplot as plt
from matplotlib import ticker

#绘制两个子图ax1和ax2
fig, ax = plt.subplots(2,1,figsize=(5,5), dpi=200)
ax1 = ax[0]
ax2 = ax[1]
ax1.bar(x=[1,2,3,4,5,6,7,8],height=[3,5,7,3,6,1,8,2])
ax2.bar(x=[1,2,3,4,5,6,7,8],height=[7,2,9,9,3,1,6,4])

# 自定义ax1的x轴刻度label
ax1.set_xticks([1,2,3,4,5,6,7,8])                       #设置需要自定义设置刻度标签的刻度位置
ax1.set_xticklabels(['A','B','C','D','E','F','G','H'])  #设置自定义刻度标签名称
# 自定义ax1的y轴刻度label
ax1.set_yticks([1,2,3,4,5,6,7,8])                       #设置需要自定义设置刻度标签的刻度位置
ax1.set_yticklabels(['A','B','C','D','E','F','G','H'])  #设置自定义刻度标签名称
ax1.invert_yaxis()                                      #从上至下阅读y轴标签，既倒序

plt.show()