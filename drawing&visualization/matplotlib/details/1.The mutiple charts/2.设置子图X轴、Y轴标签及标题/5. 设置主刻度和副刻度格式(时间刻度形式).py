'''
# 设置x轴主刻度格式
day = mdates.DayLocator(interval=2)  # 主刻度为天，间隔2天
ax.xaxis.set_major_locator(day)  # 设置主刻度
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# 设置x轴副刻度格式
hoursLoc = mdates.HourLocator(interval=20)  # 为20小时为1副刻度
ax.xaxis.set_minor_locator(hoursLoc)
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H'))
'''
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

dates =[20200601 ,20200602 ,20200603 ,20200604 ,20200605 ,20200606 ,20200607 ,20200608]
sales =[20 ,30 ,40 ,60 ,50 ,70 ,40 ,30]
# 将dates改成日期格式
x= [datetime.strptime(str(d), '%Y%m%d').date() for d in dates]

# 绘图
fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
ax.plot(x, sales, lw=2, color='#24C8B0', marker='o', ms=6, mec='#FD6174', mew=1.5, mfc='w')

# 设置x轴主刻度格式
day = mdates.DayLocator(interval=2)  # 主刻度为天，间隔2天
ax.xaxis.set_major_locator(day)  # 设置主刻度
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# 设置副刻度格式
hoursLoc = mdates.HourLocator(interval=20)  # 为20小时为1副刻度
ax.xaxis.set_minor_locator(hoursLoc)
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H'))
# 设置主刻度旋转角度和刻度label刻度间的距离pad
ax.tick_params(which='major', axis='x', labelrotation=10, labelsize=9, length=5, pad=10)
ax.tick_params(which='minor', axis='x', labelsize=8, length=3)
ax.tick_params(axis='y', labelsize=9, length=3, direction='in')

ax.text(.85, .05, 'Visualization by DataCharm', transform=ax.transAxes,
        ha='center', va='center', fontsize=4, color='black', fontweight='bold', family='Times New Roman')
#plt.savefig("F:\DataCharm\学术图表绘制\Python-matplotlib\matplotlib_time_ticks_set03.png", width=8, height=5, dpi=900,bbox_inches='tight')
# 显示图像
plt.show()