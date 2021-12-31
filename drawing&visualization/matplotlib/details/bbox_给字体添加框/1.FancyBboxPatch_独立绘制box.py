'''
class matplotlib.patches.FancyBboxPatch(xy, width, height, boxstyle='round', bbox_transmuter=<deprecated parameter>, mutation_scale=1, mutation_aspect=1, **kwargs)

!必需参数：
xy：float, float，box的左下角位置。(xy = (x, y) )
width：float，box的宽度。
height：float，box的高度。
boxstyle：box的风格，主要包括 Circle	circle	pad=0.3
                            DArrow	darrow	pad=0.3
                            LArrow	larrow	pad=0.3
                            RArrow	rarrow	pad=0.3
                            Round	round	pad=0.3, rounding_size=None
                            Round4	round4	pad=0.3, rounding_size=None
                            Roundtooth	roundtooth	pad=0.3, tooth_size=None
                            Sawtooth	sawtooth	pad=0.3, tooth_size=None
                            Square	square	pad=0.3
mutation_scale：float, default: 1，应用于框样式属性的缩放因子（例如 pad 或 rounding_size）。
mutation_aspect：float, default: 1，在突变之前，矩形的高度将被这个值压缩，而突变的框将被它的逆拉伸。例如，这允许不同的水平和垂直填充。
color:同时修改框内和框的颜色
facecolor：修改框内的颜色
edgecolor：修改框的颜色
linewidth:框的粗细
linestyle：框的风格
'''

import matplotlib.patches as mpatch
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,1,figsize=(10,10), dpi=200)
ax1 = ax[0]
fancy = mpatch.FancyBboxPatch(xy=(0,0),width=0.01,height=0.001,boxstyle='Square',facecolor='red',linewidth=2,edgecolor='black',linestyle='--')
ax1.add_patch(fancy)
plt.show()

#通过下面这个代码可以查看可以绘制的boxstyle有哪些
styles = mpatch.BoxStyle.get_styles()
print(styles)