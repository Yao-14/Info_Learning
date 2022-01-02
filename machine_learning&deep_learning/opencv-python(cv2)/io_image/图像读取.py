import cv2


def input_img(filename, flag=cv2.IMREAD_GRAYSCALE):
    """
    读取图像文件

    filename - 要加载的图像文件名(图像格式包括*.bmp, *.dib, *.jpeg, *.jpg, *.jpe, *.png, *.webp, *.pbm, *.pgm, *.ppm *.pxm,
                               *.pnm, *.sr, *.ras,  *.tiff, *.tif,  *.exr, *.hdr, *.pic...)
    flag - 指定想要图像色彩空间的格式，常用格式包括：
        -1 | cv2.IMREAD_UNCHANGED    按原样返回加载的图像
        0  | cv2.IMREAD_GRAYSCALE    将图像转换为单通道灰度图像
        1  | cv2.IMREAD_COLOR        将图像转换为 3 通道 BGR 彩色图像
        2  | cv2.IMREAD_ANYDEPTH     当输入具有相应的深度时返回16位/32位图像，否则将其转换为8位
        4  | cv2.IMREAD_ANYCOLOR     以任何可能的颜色格式读取图像

    Example:
    >> img = read_img(filename, flag=cv2.IMREAD_GRAYSCALE)
    """
    img = cv2.imread(filename=filename, flags=flag)

    if img is None:
        raise IOError("Could not read the image.")
    else:
        print(f"图像矩阵尺寸为: {img.shape}")
        print(f"图像矩阵最大值为: {img.max()}")
        print(f"图像矩阵最小值为: {img.min()}")
        print(f"图像矩阵数据类型为: {img.dtype}")
        return img

tif = "D:\BGIpy37_pytorch113\Data_lasso_ssDNA_20211230\C4\FP200000393BR_C4.tif"
img = input_img(filename=tif)
