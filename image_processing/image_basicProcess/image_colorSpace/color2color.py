import cv2


def color2color(img, code):
    """
    Convert an image from one color space to another. Commonly color space conversion codes include:
        cv2.COLOR_BGR2GRAY 
        cv2.COLOR_BGR2RGB  
        cv2.COLOR_BGR2HSV  
    To get all color space conversion codes, use codes = [i for i in dir(cv2) if i.startswith('COLOR_')].

    Args:
        img: Image matrix.
        code: Color spaces code.
    Returns:
        The image matrix after transforming the color space.

    Example:
        >>> color2color(img, code=cv2.COLOR_BGR2GRAY)
    """
    return cv2.cvtColor(img, code)
