"""Addition of images.
"""

import cv2


def imgs_add(img1=None, img2=None):
    """
    Add two images of the same size and number of channels.

    Args:
        img1: The first image matrix.
        img2: The second image matrix.
    Returns:
        The added image matrix.

    Example:
        >>> imgs_add(img1, img2)
    """
    return cv2.add(img1, img2)


def img_addWeighted(img1, img2, alpha=0.5, gamma=0):
    """
    Add two images of the same size and number of channels, and assign different weights to the images.
    Algorithm: dst = img1 * alpha + img2 * (1-alpha) + gamma

    Args:
        img1: The first image matrix.
        img2: The second image matrix.
        alpha: The weights of the first image matrix. Meanwhile the weight of the second image matrix is 1-alpha.
        gamma: scalar added to each sum.（Equivalent to adjusting the brightness, it is generally recommended to be 0.）
    Returns:
        The added image matrix.

    Example:
        >>> img_addWeighted(img1, img2, alpha=0.5, gamma=0)
    """
    return cv2.addWeighted(img1, img2, alpha, gamma)
