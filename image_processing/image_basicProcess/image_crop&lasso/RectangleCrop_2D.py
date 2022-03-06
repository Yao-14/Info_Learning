"""Enter a rectangle to crop the image.
"""
import numpy as np


def rectangle_crop(
    img: np.ndarray,
    rectangle: tuple,
) -> np.ndarray:
    """
    Enter a rectangle to crop the image.

    Args:
        img：Image matrix.
        rectangle: A tuple of four elements that determines the size and position of a rectangle.
                   rectangle[0] and rectangle[1] determine the height of the rectangle.
                   rectangle[2] and rectangle[3] determine the width of the rectangle.
    Returns:
        A cropped image.

    Example:
        >>> rectangle_crop(img, rectangle=(100, 200, 0, 100))
    """
    return img[rectangle[0]: rectangle[1], rectangle[2]:rectangle[3]]

