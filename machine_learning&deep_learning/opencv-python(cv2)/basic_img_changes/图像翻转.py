import cv2


def flip_img(src, filp_method=1):
    """
    翻转图像，翻转图像的方法包括沿X轴翻转、沿Y轴翻转、沿XY对角线翻转

    filp_method = 0     沿X轴翻转
    filp_method = 1     沿Y轴翻转
    filp_method = -1    沿XY对角线翻转

    Example:
    >> flip_img = flip_img(src, filp_method=1)
    """
    return cv2.flip(src, filp_method)
