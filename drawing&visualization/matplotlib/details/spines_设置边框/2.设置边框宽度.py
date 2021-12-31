import matplotlib.pyplot as plt
fig = plt.figure(figsize=[15,15])
ax = plt.axes()
#或ax = plt.gca()#获取边框

#设置图片上边框宽度
ax.spines['top'].set_linewidth(2)
#设置图片右边框宽度
ax.spines['right'].set_linewidth(2)
#设置图片下边框宽度
ax.spines['bottom'].set_linewidth(2)
#设置图片左边框宽度
ax.spines['left'].set_linewidth(2)
plt.show()

