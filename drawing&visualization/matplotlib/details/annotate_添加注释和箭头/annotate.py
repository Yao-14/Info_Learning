'''
用于在图形上给数据添加文本注解，而且支持带箭头的划线工具，方便我们在合适的位置添加描述信息————plt.annotate()
plt.annotate(text, xy,xytext,arrowprops)
text: 注释文本
xy:被注释的坐标点，二维元组形如(x,y)
xytext:注释文本的坐标点，也是二维元组，默认与xy相同
arrowprops：箭头的样式，dict（字典）型数据，如果该属性非空，则会在注释文本和被注释点之间画一个箭头。
    如果不设置'arrowstyle' 关键字，则允许包含以下关键字：
        width	箭头的宽度（单位是点）
        headwidth	箭头头部的宽度（点）
        headlength	箭头头部的长度（点）
        shrink	箭头两端收缩的百分比（占总长）
        facecolor 设置箭头内部颜色
        edgecolor 设置箭头边框颜色
        alpha 设置透明度
        如：arrowprops={'width':5,'headwidth':10,'headlength':10,'shrink':0.1}
    如果设置了‘arrowstyle’关键字，以上关键字就不能使用。允许的值有：
        '-'	        None
        '->'	    head_length=0.4,head_width=0.2
        '-['	    widthB=1.0,lengthB=0.2,angleB=None
        '|-|'	    widthA=1.0,widthB=1.0
        '-|>'	    head_length=0.4,head_width=0.2
        '<-'	    head_length=0.4,head_width=0.2
        '<->'	    head_length=0.4,head_width=0.2
        '<|-'	    head_length=0.4,head_width=0.2
        '<|-|>'	    head_length=0.4,head_width=0.2
        'fancy'	    head_length=0.4,head_width=0.4,tail_width=0.4
        'simple'	head_length=0.5,head_width=0.5,tail_width=0.2
        'wedge'	    tail_width=0.3,shrink_factor=0.5
        如：arrowprops={'arrowstyle':'->'}
bbox：注释文本是否添加框
    'boxstyle':设置边框样式，可选'round',
    'facecolor':设置框内部颜色
    'edgecolor': 设置框的颜色
    'linewidth':设置框的粗细
    如：bbox={'boxstyle':'round','facecolor':"white",'edgecolor':'red','linewidth':4})
verticalalignment：表示注释文本的垂直方向对齐指定位置的方式 ，可选'center'，'top'，'bottom'，'baseline'等
horizontalalignment：表示注释文本的水平方向对齐指定位置的方式  ，可选'center'，'right'，'left'等
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(0,30,size=10)
x[5] = 30  # 把索引为5的位置改为30
plt.figure(figsize=(12,6))
plt.plot(x)
plt.ylim([-2,35]) # 设置y轴的刻度
plt.annotate(text='this point is important',xy=(5,30),xytext=(7,31),
             arrowprops={'width':5,
                         'headwidth':10,
                         'headlength':10,
                         'shrink':0.1,
                         'facecolor':'red',
                         'edgecolor':'red'},
             bbox={'boxstyle':'round','facecolor':"white",'edgecolor':'red','linewidth':4})
plt.show()
