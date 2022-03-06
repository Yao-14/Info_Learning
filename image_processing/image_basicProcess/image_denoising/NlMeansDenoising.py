"""Non-local Means Denoising algorithm to remove noise in the image in OpenCV.
"""
import cv2


def non_local_means_denoising(img, h=10, templateWindowSize=7, searchWindowSize=21):
    """
    Non-local Means Denoising algorithm to remove noise in the image.
    cv2.fastNlMeansDenoising() works with a single grayscale images.
    cv2.fastNlMeansDenoisingColored() works with a color image.

    Args:
        img：Image matrix.
        h : parameter deciding filter strength. Higher h value removes noise better, but removes details of image also. (recommended 10)
        templateWindowSize : should be odd. (recommended 7)
        searchWindowSize : should be odd. (recommended 21)
    Returns:
        A denoised image matrix.
    """
    if len(img.shape == 2):
        # works with a single grayscale images
        return cv2.fastNlMeansDenoising(img, None, h=h, templateWindowSize=templateWindowSize,
                                        searchWindowSize=searchWindowSize)
    else:
        # works with a color image.
        return cv2.fastNlMeansDenoisingColored(img, None, h=h, hColor=h,templateWindowSize=templateWindowSize,
                                               searchWindowSize=searchWindowSize)
