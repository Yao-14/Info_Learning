import cv2


def gray2color(img, code):
    """
    Convert a grayscale image to a pseudo-color image. Pseudo color spaces include:
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

    Args:
        img: Image matrix.
        code: Pseudo color spaces code.
    Returns:
        The image matrix after transforming the color space.

    Example:
        >>> gray2color(img, code=cv2.COLORMAP_JET)
    """
    return cv2.applyColorMap(img, code)
