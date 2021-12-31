
'''******** 图片的加载 ---- 获得一个RGB三通道的矩阵数据 ********'''
import skimage.io as io
image1 = io.imread("./Example_Image/image1.jpg")
print(image1)

'''******** 图片的数字矩阵格式 ********'''
import numpy as np
# 图片矩阵 ---- .shape ：（300, 451, 3）代表该图片是一个长300，宽451，3通道的图片。
print(image1.shape)
# 图片像素强度 ---- numpy.min(), numpy.max(), numpy.mean() ：min=0，max=222，mean=115代表该图片的像素强度在0到222之间（最大范围是0到255）,平均像素强度在115左右。
print(np.max(image1)); print(np.min(image1)); print(np.mean(image1))
# 查看图像各个通道的矩阵
print(image1[:,:,0]) # 查看R通道矩阵（红色）
print(image1[:,:,1]) # 查看G通道矩阵（绿色）
print(image1[:,:,2]) # 查看B通道矩阵（蓝色）
