import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
'''方法1：ax=plt.axes([0.14, 0.35, 0.77, 0.6]) #[x,y,width,height] 规定的矩形区域 （全部是0~1之间的数，表示比例）
        创建各个子图的坐标轴，传入一个四元列表参数：[x,y,width,height]，用来表示这个子图坐标轴原点的x坐标、y坐标，以及宽和高。
        这四个值的取值范围都是[0,1]，我们约定整个大图的左下端为原点(0,0)，右上端为(1,1)。那么x,y的取值就表示该子图坐标原点的横
        坐标值和纵坐标值占大图整个长宽的比例。而width和height则表示子图的宽和高占整个大图的宽和高的比例。如果不传入参数则表示选
        取默认坐标轴，即大图的坐标轴
   方法1的好处：可以实现子图里面再绘制一个子图
'''
fig1 = plt.figure(figsize=[10,10],dpi=200)
ax10 = plt.axes()
ax11 = plt.axes([0.3, 0.45, 0.4, 0.4])
ax12 = plt.axes([0.3, 0.2, 0.4, 0.2])
fig1.show()

'''方法2-1：通过gs=gridspec.GridSpec()创建区域,而后通过plt.subplot(gs[:,:])创建子图'''#比较推荐使用！！！！
fig2 = plt.figure(figsize=(10,10),dpi=200)
gs2=gridspec.GridSpec(100,3) #通过gridspec.GridSpec()创建区域，（100，3）相当于将区域平均分为100行3列这300个小区域（等大）
ax21=plt.subplot(gs2[0:50,:])#gs[0:50,:]里表示区域中1-50行和1-3列这150个小区域共同组成子图1
ax22=plt.subplot(gs2[60:100,1:])#gs[0:50,:]里表示区域中60-100行和2-3列这80个小区域共同组成子图2
fig2.show()
'''方法2-2：通过gridspec.GridSpec(2, 2,width_ratios=[1,2],height_ratios=[4,1])创建2行2列4个区域，但这四个区域不是等大的，四个区域的大小由width_ratios和height_ratios控制
            width_ratios=[1,2]：指创建的四个区域，宽度比是1：2
            height_ratios=[4,1]：指创建的四个区域，高度比是4：1
'''
fig3 = plt.figure(figsize=(10,10),dpi=200)
gs3 = gridspec.GridSpec(2, 2,width_ratios=[1,2],height_ratios=[4,1]) #创建2行2列4个区域，但这四个区域不是等大的，四个区域的大小由width_ratios和height_ratios控制
ax31 = plt.subplot(gs3[0])
ax32 = plt.subplot(gs3[1])
ax33 = plt.subplot(gs3[2])
ax34 = plt.subplot(gs3[3])
fig3.show()
'''方法2-3：嵌套使用GridSpec'''
fig4 = plt.figure(figsize=(10,10),dpi=200)
gs4 = gridspec.GridSpec(1, 2) #通过gridspec.GridSpec()创建区域，创建1行2列两个中区域（等大）
gs40 = gridspec.GridSpecFromSubplotSpec(3, 3, subplot_spec=gs4[0])  #通过gridspec.GridSpecFromSubplotSpec()在gs[0]这个中区域中创建3行3列九个小区域（等大）
gs41 = gridspec.GridSpecFromSubplotSpec(3, 3, subplot_spec=gs4[1])  #通过gridspec.GridSpecFromSubplotSpec()在gs[1]这个中区域中创建3行3列九个小区域（等大）
ax401 = plt.subplot(gs40[0])
ax402 = plt.subplot(gs40[1])
ax403 = plt.subplot(gs40[2])
ax411 = plt.subplot(gs41[0])
ax412 = plt.subplot(gs41[1])
ax413 = plt.subplot(gs41[2])
fig4.show()