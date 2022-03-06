import cv2


def color2color(src, code):
    """
    将图像从一种颜色空间转换为另一种颜色空间，通过色彩空间转换代码实现。常用的色彩空间转换代码包括：
    cv2.COLOR_BGR2GRAY  - BGR 转换成灰度图
    cv2.COLOR_BGR2RGB   - BGR 转换成 RGB
    cv2.COLOR_BGR2HSV   - BGR 转换成 HSV
    (最经常使用BGR2XXX的原因是cv2.imread()接口读取的图像格式是BGR)
    若想获得所有色彩空间转换代码，可使用 codes = [i for i in dir(cv2) if i.startswith('COLOR_')]

    Example:
    >> grey_img = color2color(src, code=cv2.COLOR_BGR2GRAY)
    """
    return cv2.cvtColor(src, code)


def gray2color(src_gray, code):
    """
    将灰度图转换为伪色彩图。伪色彩空间包括：
    cv2.COLORMAP_AUTUMN
    cv2.COLORMAP_BONE
    cv2.COLORMAP_JET
    cv2.COLORMAP_WINTER
    cv2.COLORMAP_RAINBOW
    cv2.COLORMAP_OCEAN
    cv2.COLORMAP_SUMMER
    cv2.COLORMAP_SPRING
    cv2.COLORMAP_COOL
    cv2.COLORMAP_HSV
    cv2.COLORMAP_PINK
    cv2.COLORMAP_HOT

    Example:
    >> color_img = gray2color(src_gray, code=cv2.COLORMAP_JET)
    """
    return cv2.applyColorMap(src_gray, code)

