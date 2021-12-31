
'''******** 图片的加载 ---- 获得一个RGB三通道的矩阵数据 ********'''
import skimage.io as io
image1 = io.imread("./Example_Image/image1.jpg")

'''******** 图片颜色空间转化1 ---- 压缩三通道三维矩阵为1通道的二维矩阵，将RGB图片转化为灰度图像 ********'''
import matplotlib.pyplot as plt
import numpy as np
# 方法1 ---- 手动转化
image1_gray1 = np.mean(image1,2)
print(image1_gray1.shape)
plt.imshow(image1_gray1);plt.show()
# 方法2 ---- 使用skimage内置函数 rgb2gray 转化
from skimage.color import rgb2gray
image1_gray2 = rgb2gray(image1)
plt.imshow(image1_gray2);plt.show()
# 注意事项：灰度图展示出来不是真正的灰度图，而是亮度图。因此若要展示灰度图可以使用plt.cm.gray
plt.imshow(image1_gray2,plt.cm.gray);plt.show()

'''******** 图片颜色空间转化2 ---- 将RGB图像转化为HSV图像 ********'''
# 色相(H)：色彩的基本属性，就是平常所说的颜色名称，如红色、黄色等。
# 饱和度(S)：指色彩的纯度，越高色彩越纯，越低色彩越灰，取0-100%的数值。
# 明度(V)：即亮度，取0-100%的数值。
# 使用skimage内置函数 rgb2hsv 转化
from skimage.color import rgb2hsv
image1_hsv = rgb2hsv(image1)
plt.imshow(image1_hsv);plt.show()

'''******** 图片颜色空间转化3 ---- 将HSV图像转化为RGB图像 ********'''
# 使用skimage内置函数 hsv2rgb 转化
from skimage.color import hsv2rgb
image1_hsv2rgb = hsv2rgb(image1_hsv)
plt.imshow(image1_hsv2rgb);plt.show()

'''******** 图片颜色空间转化4 ---- 图像亮度变化 ********'''
# 使用skimage内置函数 exposure 转化
from skimage import exposure
img_g=exposure.adjust_gamma(image1,.1) # 数据越大图片越暗，数据越小图片越亮
plt.imshow(img_g);plt.show()