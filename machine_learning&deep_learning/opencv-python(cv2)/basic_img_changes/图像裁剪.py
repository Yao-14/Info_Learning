import cv2


def rectangle_crop_img(src, x_start, x_end, y_start, y_end):
    """
    矩形裁剪tif图像中需要的部分

    图像 (0, 0)点位于图像的左上角
    x_start和x_end确定图像的高度
    y_start和y_end确定图像的宽度

    Example:
    >> crop_img = rectangle_crop_img(src, x_start=4000, x_end=9000, y_start=6000, y_end=11000)
    """
    return src[x_start: x_end, y_start:y_end]
