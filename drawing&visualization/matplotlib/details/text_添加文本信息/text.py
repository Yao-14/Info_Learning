'''
添加文本信息————plt.text
plt.text(x, y, s, fontsize, verticalalignment,horizontalalignment,rotation , **kwargs)
x,y：表示标签添加的位置
s：展示的字符串文本
fontsize：标签字体大小，取整数
verticalalignment：表示垂直对齐方式 ，可选'center'，'top'，'bottom'，'baseline'等
horizontalalignment：表示水平对齐方式 ，可以填'center'，'right'，'left'等
rotation：表示标签的旋转角度，以逆时针计算，取整
family： 用来设置字体，如：'Times New Roman'
style： 设置字体的风格，如：'italic'
weight： 字体的粗细, 如：'light'
bbox： 给字体添加框,如 bbox=dict(facecolor='red', alpha=0.5)
'''
import matplotlib.pyplot as plt
import numpy as np
plt.bar([1,2,3,4,5],[8,14,17,23,30],color = 'b',width = 0.3,label = '1oooooo')
for x,y in zip([1,2,3,4,5],[8,14,17,23,30]):
    plt.text(x,y+1, y,
         fontsize = 10,
         verticalalignment='center',
         horizontalalignment='center',
         rotation = 30 ,
         weight = 'bold')
plt.show()