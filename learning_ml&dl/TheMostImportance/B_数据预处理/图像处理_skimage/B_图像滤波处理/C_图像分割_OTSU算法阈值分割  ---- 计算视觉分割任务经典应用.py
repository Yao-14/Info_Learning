'''

************ 基于OTSU算法的阈值分割方法 ———— 图像分割的最基础的方法 ************
1.把图像转成灰度图
2.计算全部平均灰度w
3.选定一个阈值T把所有像素分成N0,N1两个
4.计算N0的灰度w0,N1的灰度w1
5.计算类间方差g = N0*(w0-w)^2 + N1*(w1-w)^2
6.采用遍历法找到Tmax使得g最大

************ OTSU算法阈值分割的代码实现 ************
import skimage.filters as filters
theta=filters.threshold_otsu(img_gray,nbins=256)
img_seg=np.zeros(img_gray.shape)
img_seg[img_gray>theta]=1

'''

import skimage.io as io
import skimage.filters as filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import numpy as np

# 导入图像
image = io.imread("./Example_Image/4.jpg")
# 将图像转化成灰度图
img_gray= rgb2gray(image)

#采用otsu算法计算分割阈值
theta=filters.threshold_otsu(img_gray,nbins=256)
print(theta)
#通过阈值生成分割的图片
img_seg=np.zeros(img_gray.shape)
img_seg[img_gray>theta]=1
plt.imshow(img_seg);plt.show()

# 测试不同nbins效果并展示
theta=filters.threshold_otsu(img_gray,nbins=2)
img_seg1=np.zeros(image.shape)
img_seg1[img_gray>theta]=1

theta = filters.threshold_otsu(img_gray,nbins=256)
img_seg2=np.zeros(image.shape)
img_seg2[img_gray>theta]=1
print(img_seg)
plt.figure('segmented_img',figsize=(15,5))
plt.subplot(131);plt.imshow(img_seg)
plt.subplot(132);plt.imshow(img_seg1)
plt.subplot(133);plt.imshow(img_seg2)
plt.show()
