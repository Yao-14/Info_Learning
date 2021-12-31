import matplotlib.pyplot as plt
fig = plt.figure(figsize=[15,15])
ax = plt.axes()
#隐藏图片上面的框
ax.spines['top'].set_visible(False)
#隐藏图片右面的框
ax.spines['right'].set_visible(False)
#隐藏图片下面的框
ax.spines['bottom'].set_visible(False)
#隐藏图片左面的框
ax.spines['left'].set_visible(False)
#隐藏所有边框
plt.axes('off')
plt.show()

