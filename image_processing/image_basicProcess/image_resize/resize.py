"""Scale the image, change the size of the image.
"""
import cv2


def img_resize(img, new_size=None, fx=None, fy=None):
    """
    Scale the image, change the size of the image.

    Args:
        img: Image matrix.
        new_size: The size of the scaled image.
        fx: The scale by which the image is scaled on the x-axis. (Only valid when new_size==0)
        fy: The scale by which the image is scaled on the y-axis. (Only valid when new_size==0)
    Returns:
        A scaled image matrix.

    Example:
        >>> img_resize(img, new_size=(346, 301), fx=None, fy=None)
        >>> img_resize(img, new_size=None, fx=0.5, fy=0.5)
    """

    return cv2.resize(img, new_size, fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
