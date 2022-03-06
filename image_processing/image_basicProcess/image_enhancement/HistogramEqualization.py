"""
图像增强主要解决由于图像的灰度级范围较小造成的对比度较低的问题，目的就是将输出图像的灰度级放大到指定的程度，使得图像中的细节看起来增加清晰。
对比度增强有几种常用的方法，如线性变换、分段线性变换、伽马变换、直方图正规化、直方图均衡化、局部自适应直方图均衡化等。
"""

import cv2


def equalhist_transfer(img, method="global", cliplimit=20):
    """
    Histogram equalization for image enhancement, including:
        global histogram equalization,
        adaptive local histogram equalization.

    Args:
        img: Single-channel uint8 type grayscale image[0, 255].
        method: Histogram equalization methods. Available `method` are:
            * `'global'`: global histogram equalization;
            * `'local'`: adaptive local histogram equalization.
        cliplimit: Threshold to limit contrast when method = 'local' .
    Returns:
        Image matrix after image enhancement.

    Example:
        >>> equalhist_transfer(img, method="global")
        >>> equalhist_transfer(img, method="local", clipLimit=10)
    """
    if method == "global":
        # Global histogram equalization.
        return cv2.equalizeHist(img)
    elif method == "local":
        # Adaptive local histogram equalization.
        clahe = cv2.createCLAHE(clipLimit=cliplimit, tileGridSize=(7, 7))
        return clahe.apply(img)
    else:
        raise ValueError(
            f"Available histogram equalization methods are `global` and `local`."
        )
