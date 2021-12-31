''' Axes.invert_yaxis(self) —————将Y轴调换方向
    Axes.invert_xaxis(self) —————将X轴调换方向
'''
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2,1)
#y轴从上至下是C、B、A
axes[0].barh(y=[1,2,3],width=[10,10,10],height=[0.1,0.2,0.3],color=['red','green','blue'],align='center',tick_label=['A','B','C'])
#通过invert_yaxis()使y轴从上至下是A、B、C
axes[1].barh(y=[1,2,3],width=[10,10,10],height=[0.1,0.2,0.3],color=['red','green','blue'],align='center',tick_label=['A','B','C'])
axes[1].invert_yaxis()  # labels read top-to-bottom

plt.show()