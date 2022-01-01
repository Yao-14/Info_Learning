import cv2


def resize_img(src, new_size=None, fx=None, fy=None):
    """
    缩放图像，改变图像大小

    方法1：输入新图像的大小
    Example:
    >> resize_img = resize_img(src, new_size=(346, 301))
    方法2：当new_size=None时，输入缩放图像的比例，按比例改变图像大小
    Example:
    >> resize_img = resize_img(src, fx=0.5, fy=0.5)
    """
    return cv2.resize(src, new_size, fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
