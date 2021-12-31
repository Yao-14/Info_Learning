'''全局范围内共享不同子图的坐标轴————必须使用plt.subplots()绘制子图
   subplots()函数有两个共享坐标轴参数sharex和sharey，有四种取值'row'、'col'、'all'、'none'
   共享坐标轴后若想将共享坐标轴的子区之间的空隙去掉，则加上plt.subplots_adjust(hspace=0, wspace=0)即可
'''
import matplotlib.pyplot as plt
fig1, axes = plt.subplots(2, 2, figsize=(10,10),dpi=100,sharex='all',sharey='all')
fig1.subplots_adjust(wspace=0,hspace=0)
fig1.show()

'''共享个别子图的坐标轴————必须使用plt.subplot()绘制子图'''
import matplotlib.pyplot as plt
fig2= plt.figure(figsize=(10,10),dpi=100)
ax21 = plt.subplot(2,2,1)
ax22 = plt.subplot(2,2,2)
ax23 = plt.subplot(2,2,3)
ax24 = plt.subplot(2,2,4,sharex=ax21) #ax24通过sharex共享ax21的x坐标轴
fig2.show()