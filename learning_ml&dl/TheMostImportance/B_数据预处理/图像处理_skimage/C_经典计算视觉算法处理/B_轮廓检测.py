'''

************ 轮廓检测 ---- 代码实现 ************
import skimage.measure as measure
measure.find_contours(image,0.5)        轮廓检测，输入一个图片，搜索图片轮廓的强度
'''

import skimage.measure as measure
import skimage.draw as draw
import numpy as np
import matplotlib.pyplot as plt
#画图
img=np.zeros([200,200])
#画一圆
h,w=draw.disk(center=(150,50),radius=30)
img[h,w]=1
#画一个正方形
img[40:60,60:80]=1

# 轮廓检测
contours=measure.find_contours(img,0)
# 可视化
plt.figure("detetct contours",figsize=(8,8))
plt.subplot(121);plt.imshow(img)
plt.subplot(122);plt.imshow(img)
for i in range(len(contours)):
    array1 = contours[i]
    plt.plot(array1[:,1],array1[:,0],linewidth=2)

plt.show()