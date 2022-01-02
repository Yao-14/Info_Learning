"""
图像增强主要解决由于图像的灰度级范围较小造成的对比度较低的问题，目的就是将输出图像的灰度级放大到指定的程度，使得图像中的细节看起来增加清晰。
对比度增强有几种常用的方法，如线性变换、分段线性变换、伽马变换、直方图正规化、直方图均衡化、局部自适应直方图均衡化等。
"""

import numpy as np
import cv2

def gamma_transfer(src, gamma=0.5):
    """
    伽马变换：将一张图的灰度值归至[0,1]后，对像素值做幂次方变换，主要是图像的灰度级发生改变

    src - 单通道的uint8类型灰度图[0, 255]
    当 gamma=1 时图像不发生变换
    当 0<gamma<1 时增强图像的对比度
    当 1<gamma 时降低图像的对比度

    Example:
    >> dst = gamma_transfer(src, gamma=0.5)
    """
    img = 255 * np.power(src / 255, gamma)
    img = np.around(img)
    img[img > 255] = 255
    return img.astype(np.uint8)

def equalhist_transfer(src, method="global", clipLimit=10):
    """
    全局直方图均衡化：
    处理图像对比度，使得图像整体效果均匀，黑与白之间的各个像素级之间的点更均匀。通过这种方法，亮度可以更好地在直方图上分布。
    可以用于增强局部的对比度而不影响整体的对比度，直方图均衡化通过有效地扩展常用的亮度来实现这种功能。
    这种方法对于背景和前景都太亮或者太暗的图像非常有用，以及曝光过度或者曝光不足照片中更好的细节。

    局部直方图自适应均衡化：
    自适应直方图均衡化将图像划分为不重叠的小块，在每一块进行直方图均衡化，如果小块内有噪声，则影响就会很大，需要通过限制对比度来进行抑制。即通过对比度自适应直方图均衡化。
    如果限制对比度的阈值设置为40，那么在图像中像素值出现次数大于40的次数就会将大于40的部分像素点去掉，平均成其它的像素点。

    src - 单通道的uint8类型灰度图[0, 255]
    method - `global` or `local`， 全局直方图均衡化或局部直方图自适应均衡化
    clipLimit - 当 method = "local" 时，限制对比度的阈值。

    Example:
    >> dst = equalhist_transfer(src, method="global")
    >> dst = equalhist_transfer(src, method="local", clipLimit=10)
    """
    # 全局直方图均衡化
    if method == "global":
        return cv2.equalizeHist(src)
    # 局部直方图自适应均衡化（如果全局直方图均衡化效果不好则使用局部直方图自适应均衡化，并调整clipLimit的大小）
    elif method == "local":
        clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=(7, 7))
        return clahe.apply(src)


