"""
图像增强主要解决由于图像的灰度级范围较小造成的对比度较低的问题，目的就是将输出图像的灰度级放大到指定的程度，使得图像中的细节看起来增加清晰。
对比度增强有几种常用的方法，如线性变换、分段线性变换、伽马矫正（伽马变换）、直方图正规化、直方图均衡化、局部自适应直方图均衡化等。
"""

import numpy as np


def gamma_correction(img, gamma=0.5):
    """
    Gamma correction is also known as the Power Law Transform.
    First, our image pixel intensities must be scaled from the range [0, 255] to [0, 1.0].
    From there, we obtain our output gamma corrected image by applying the following equation:
        Gamma values < 1 will shift the image towards the darker end of the spectrum;
        Gamma values > 1 will make the image appear lighter;
        Gamma value = 1 will have no affect on the input image.

    Args:
        img: Single-channel uint8 type grayscale image[0, 255].
        gamma: Gamma values.
               Gamma values < 1 will shift the image towards the darker end of the spectrum;
               Gamma values > 1 will make the image appear lighter.
               Gamma value = 1 will have no affect on the input image.

    Returns:
        Image matrix after image enhancement.

    Example:
        >>> gamma_correction(img, gamma=0.5)
    """
    img = 255 * np.power(img / 255, gamma)
    img = np.around(img)
    img[img > 255] = 255
    return img.astype(np.uint8)