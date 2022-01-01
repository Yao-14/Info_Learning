
import os
import cv2


tif = "D:\BGIpy37_pytorch113\Data_lasso_ssDNA_20211230\C4\FP200000393BR_C4.tif"
img = cv2.imread(tif, 2)
#第二个参数是通道数和位深的参数:
# -1 = IMREAD_UNCHANGED  # 不进行转化，比如保存为了16位的图片，读取出来仍然为16位。
# 0 = IMREAD_GRAYSCALE   # 进行转化为灰度图，比如保存为了16位的图片，读取出来为8位，类型为CV_8UC1。
# 1 = IMREAD_COLOR =     # 进行转化为RGB三通道图像，图像深度转为8位
# 2 = IMREAD_ANYDEPTH    # 保持图像深度不变，进行转化为灰度图。
# 4 = IMREAD_ANYCOLOR    # 若图像通道数小于等于3，则保持原通道数不变；若通道数大于3则只取取前三个通道。图像深度转为8位
print(img)
print(img.shape)
print(img.dtype)
print(img.min())
print(img.max())

#创建窗口并显示图像
# 创建窗口
cv2.namedWindow("Image", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
# 设定窗口大小
cv2.resizeWindow("Image", 1024, 768)
# 显示图像
cv2.imshow("Image", img)
cv2.waitKey(0)
# 释放窗口
cv2.destroyAllWindows()