'''
************ 图像滤波简介 ************
图像预处理之图像滤波：指通过卷积方法运用特定手段消除图像中混入的噪音，为图像识别抽取出图像特征。————两个作用分别依赖于平滑滤波和边缘检测

************ 平滑滤波 ———— 降噪 ************
平滑滤波实现方法1：简单平均法 ———— 不好
平滑滤波实现方法2：高斯滤波  ———— 好，第一选择

************ 高斯滤波代码实现 ************
from skimage.filters import gaussian
image = gaussian(image,sigma)   # 输入的image为灰度图像，sigma指用于卷积运算的算子的大小(sigma越大，图像越模糊，即降噪程度越大）

'''
# 图片平滑滤波-高斯滤波

import skimage.io as io
import skimage.filters as filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
# 导入图像
image = io.imread("./Example_Image/4.jpg")
# 将图像转化成灰度图
img_gray= rgb2gray(image)
# 展示灰白灰度图而不是亮度灰度图
plt.imshow(img_gray,plt.cm.gray);plt.show()
# 调用gaussian模块计算高斯滤波（尝试不同的sigma=1,3,10感受效果）
img_e1 = filters.gaussian(img_gray,sigma=1)
img_e2 = filters.gaussian(img_gray,sigma=3)
img_e3 = filters.gaussian(img_gray,sigma=10)
print(img_e2)
plt.imshow(img_e1);plt.show();plt.imshow(img_e2);plt.show();plt.imshow(img_e3);plt.show()