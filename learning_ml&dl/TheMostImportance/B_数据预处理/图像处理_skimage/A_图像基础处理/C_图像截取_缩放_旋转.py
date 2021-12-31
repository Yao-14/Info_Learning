
'''******** 图片的加载 ---- 获得一个RGB三通道的矩阵数据 ********'''
import matplotlib.pyplot as plt
import skimage.io as io
import numpy as np
image1 = io.imread("./Example_Image/image1.jpg")
image1_heigh = image1.shape[0] # 图片y轴长度为300
image1_width = image1.shape[1]  # 图片x轴长度为451

'''******** 图片的截取 ********'''
# 在image1上截取一个y轴长为50，x轴长为100的图片
image1_s1 = image1[50:100,100:200,:]
plt.imshow(image1_s1) ; plt.show()

'''******** 图片的缩放 ---- 通过skimage内置函数 transform.resize 实现 ********'''
from skimage import transform
# 将图片压缩成100x100大小
img_r=transform.resize(image1,output_shape=[100,100])
plt.imshow(img_r);plt.show()
# 将图片放大成500x500大小
img_r=transform.resize(image1,output_shape=[500,500])
plt.imshow(img_r);plt.show()

'''******** 图片的旋转 ---- 通过skimage内置函数 transform.rotate 实现绘制对数据相对较大的图像进行压缩 ********'''
# 将图片逆时针选择45度，并且使图片适应画布
img_r=transform.rotate(image1,45,resize=True)
plt.imshow(img_r);plt.show()