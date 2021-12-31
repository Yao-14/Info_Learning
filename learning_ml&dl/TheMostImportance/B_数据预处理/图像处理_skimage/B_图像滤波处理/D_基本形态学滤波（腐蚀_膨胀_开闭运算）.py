'''

************ 基本形态学滤波 ———— 膨胀，腐蚀，开闭运算 ************
    膨胀：类似于'领域扩张' ,将图像的高亮区域或白色部分进行扩张,其运行结果图比原图的高亮区域更大.
    腐蚀：类似于'领域被蚕食' ,将图像中的高亮区域或白色部分进行缩减细化,其运行结果图比原图的高亮区域更小。
    开运算：先腐蚀再膨胀。
    闭运算：先膨胀再腐蚀。

************ 基本形态学滤波 ———— 膨胀，腐蚀，开闭运算作用总结 ************
    对二值化图像(0,1)：去掉像素用腐蚀，开运算；增加像素用膨胀，闭运算
    对灰度图像：灰度值降低，用腐蚀，开运算；灰度值增加用膨胀，闭运算

************ 基本形态学滤波 ———— 膨胀，腐蚀，开闭运算的代码实现 ************
    from skimage import morphology
    膨胀：morphology.dilation(img,morpholoy.square(2))
    腐蚀：morphology.erosion(img,morpholoy.square(2))
    开运算：morphology.opening(img_gray,morpholoy.square(5))
    闭运算：morphology.closing(img_gray,morpholoy.square(5))

'''


#基本形态学滤波，载入必要的模块和图片
import skimage.io as io
from skimage import morphology
from skimage import transform
from skimage import data
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

'''************ 开运算 ************'''
#载入一张特别的图片方便理解
img=io.imread("./Example_Image/5.jpg")
img=transform.resize(img,[100,150])

#清理一下，把图片二值化
img_gray=rgb2gray(img)
img_gray[img_gray>0.5]=1
img_gray[img_gray<0.5]=0

#开运算，先腐蚀再膨胀，可以消除小物体小斑块
img_d=morphology.erosion(img_gray,morphology.square(25))
img_d=morphology.dilation(img_d,morphology.square(25))

plt.figure('morphology',figsize=(8,8))
plt.subplot(121);plt.imshow(img_gray)
plt.subplot(122);plt.imshow(img_d)
plt.show()

#开运算，先腐蚀再膨胀，可以消除小物体小斑块：直接调用模组，尝试不同的范围阈值
img_d=morphology.opening(img_gray,morphology.square(25))
plt.figure('morphology',figsize=(8,8))
plt.subplot(121);plt.imshow(img_gray)
plt.subplot(122);plt.imshow(img_d)
plt.show()

'''************ 闭运算 ************'''
#闭运算，先膨胀再腐蚀，可以来填充孔洞，载入特别图片方便理解
img=io.imread("./Example_Image/6.jpg")
img=transform.resize(img,[100,150])

#清理一下，把图片二值化
img_gray=rgb2gray(img)
img_gray[img_gray>0.5]=1
img_gray[img_gray<0.5]=0

#分开两步实现
img_d=morphology.dilation(img_gray,morphology.square(10))
img_d=morphology.erosion(img_d,morphology.square(10))
plt.figure('morphology',figsize=(8,8))
plt.subplot(121);plt.imshow(img_gray)
plt.subplot(122);plt.imshow(img_d)
plt.show()

#一步调用模块实现，尝试不同的范围阈值
img_d=morphology.closing(img_gray,morphology.square(10))

plt.figure('morphology',figsize=(8,8))
plt.subplot(121);plt.imshow(img_gray)
plt.subplot(122);plt.imshow(img_d)
plt.show()