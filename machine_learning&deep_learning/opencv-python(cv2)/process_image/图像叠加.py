import cv2


def add_img(src1=None, src2=None):
    """
    叠加两个相同大小和通道数的图像。

    Example:
    >> dst = add_img(src1, src2)
    """
    return cv2.add(src1, src2)


def addWeighted_img(src1=None, alpha=0.5, src2=None, beta=0.5, gamma=0):
    """
    叠加两个相同大小和通道数的图像，并对图像赋予不同的权重（0到1之间），使得它具有混合感或透明感。此函数可以用一下矩阵表达式来代替：
    dst = src1 * alpha + src2 * beta + gamma

    alpha - 第一个数组元素的权重。
    beta – 第二个数组元素的权重，一般即等于 1-alpha。
    gamma – 添加到每个总和的标量（一般默认为0即可）。

    Example:
    >> dst = addWeighted_img(src1=src1, alpha=0.5, src2=scr2, beta=0.5, gamma=0)
    """
    return cv2.addWeighted(src1, alpha, src2, beta, gamma)
