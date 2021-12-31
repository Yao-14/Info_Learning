'''方法1：通过fig, axes = plt.subplots(3, 3, figsize=(6, 6))————直接创建9个大小相等的子图'''
import matplotlib.pyplot as plt
fig1, axes = plt.subplots(3, 3, figsize=(6, 6),dpi=100)
ax1 = axes[0,0]
ax1.bar(x=1,height=10)
ax2 = axes[1,1]
ax2.bar(x=1,height=10)
ax3 = axes[2,2]
ax3.bar(x=1,height=10)
plt.tight_layout()
fig1.show()

'''方法2：通过ax1 = plt.subplot(2,2,1)一个一个创建子图'''
fig2 =  plt.figure(figsize=(6,6))
ax21 = plt.subplot(3,2,1)
ax22 = plt.subplot(3,2,3)
fig2.show()