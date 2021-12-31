import matplotlib.pyplot as plt
import numpy as np
#设置图例————label = '1oooooo'
plt.bar(np.arange(5),[8,14,17,23,30],color = 'k',width = 0.3,label = '1oooooo')
plt.bar(np.arange(5),[10,16,7,23,20],color = 'b',width = 0.3,label = '2oooooo',bottom=[8,14,17,23,30])
plt.bar(np.arange(5),[1,6,7,3,2],color = 'r',width = 0.3,label = '3oooooo',bottom=[18,30,24,46,50])
plt.bar(np.arange(5),[5,10,2,1,12],color = 'orange',width = 0.3,label = '4oooooo',bottom=[19,36,31,49,52])

'''
#图例参数设置————plt.legend()
一、图例位置设置——loc=
    设置大概的图例位置
    左上 loc='upper left'       正上 loc='upper center'       右上 loc='upper right'  
    正左 loc='center left'      正中 loc='center'             正右 loc='center right'
    左下 loc='lower left'       正下 loc='lower center'       右下 loc='lower right' 
    自动识别位于最佳位置 loc='best'
二、图例位置微调——bbox_to_anchor=(num1, num2)
    num1用于控制legend的左右移动，值越大越向右边移动，num2用于控制legend的上下移动，值越大，越向上移动。用于微调图例的位置
    一般用于要将图例放在图外可用该参数调整位置
三、图例字体大小设置——fontsize=
    int or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
    可以直接输入数字设置图例大小（如fontsize=10）
    或者输入自带7种图例大小（如fontsize='small'）
四、图例字体颜色设置——labelcolor=
    有效的颜色字符串（如labelcolor="red",设置全部字体的颜色为红色）
    或颜色字符串列表（如labelcolor=["red","blue"]，分别设置不同字体的颜色，第一个为红色、第二个为蓝色）
五、图例列数设置——ncol= 
    可以直接输入数字设置图例列数（如ncol=2）
六、设置图例标题
    图例标题名——title = 'title'
    图例标题字体大小——title_fontsize=
        int or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
七、设置图例边框及背景
    去掉图例边框——frameon=False（有边框则设置frameon=True）
    设置图例边框颜色——edgecolor = 'blue' 
    设置图例背景颜色——facecolor = 'blue' （若无边框,参数无效）
'''
plt.legend(loc='upper left',
            bbox_to_anchor=(1, 1),
            fontsize=5,
            labelcolor=['k',"blue","red",'orange'],
            ncol=2,
            title = 'title',title_fontsize= 10,
            frameon=False
           )
plt.show()
