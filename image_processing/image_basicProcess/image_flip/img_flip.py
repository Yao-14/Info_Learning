"""Flip the image
"""
import cv2


def img_flip(img, filp_method=1):
    """
    Flip the image, the methods of flipping the image include flipping along the X axis,
    flipping along the Y axis, and flipping along the XY diagonal.

    Args:
        img: Image matrix.
        filp_method: The way to flip the image. Available `filp_method` are:
            * `0`: flipping along the X axis;
            * `1`: flipping along the Y axis;
            * `-1`: flipping along the XY diagonal.
    Returns:
        A flipped image matrix.

    Example:
        >>> img_flip(img, filp_method=1)
    """
    return cv2.flip(img, filp_method)
