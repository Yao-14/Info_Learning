import matplotlib.pyplot as plt


plt.axhline(y=.3, c="r", ls="--", lw=2)
plt.axvline(x=4.0, c="r", ls="--", lw=2)
'''
plt.axhline:绘制平行于x轴的水平参考线
y：水平参考线的出发点
c：参考线的线条颜色
ls：参考线的线条风格,风格包括'-','--','-.',':','None',']'
lw：参考线的线条宽度

plt.axvline:绘制平行于y轴的水平参考线
x：水平参考线的出发点
c：参考线的线条颜色
ls：参考线的线条风格,风格包括'-','--','-.',':','None',']'
lw：参考线的线条宽度
'''
plt.show()