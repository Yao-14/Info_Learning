import cv2


def non_local_means_denoising(src, h=10, templateWindowSize=7, searchWindowSize=21):
    """
    非局部平均去噪
    cv2.fastNlMeansDenoising()              - 用于灰度图像
    cv2.fastNlMeansDenoisingColored()       - 用于彩色图像

    src - 图像矩阵
    h - 决定滤波器强度的参数。较高的 h 值可以更好地去除噪声，但也会去除图像的细节。（推荐10）
    templateWindowSize -  (recommended 7)
    searchWindowSize -  (recommended 21)
    """
    if len(src.shape == 2):
        # 用于灰度图像
        return cv2.fastNlMeansDenoising(src, None, h=h, templateWindowSize=templateWindowSize,
                                        searchWindowSize=searchWindowSize)
    else:
        # 用于彩色图像
        return cv2.fastNlMeansDenoisingColored(src, None, h=h, hColor=h,templateWindowSize=templateWindowSize,
                                               searchWindowSize=searchWindowSize)

