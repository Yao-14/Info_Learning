import cv2
import numpy as np


def output_img(
    img: np.ndarray,
    filename: str = None,
    window_size: tuple = (1024, 1024),
    show_img: bool = True
):
    """
    Output the image matrix as a 2D image file.

    Args:
        img：image matrix.
        filename: Output image filename, the end of which can be .bmp, .dib, .jpeg, .jpg, .jpe, .png, .webp, .pbm,
                  .pgm, .ppm, .pxm, .pnm, .sr, .ras, .tiff, .tif, .exr, .hdr, .pic, etc.
        window_size: The size of the image visualization window.
        show_img: Whether to create a window to display the image.

    Example:
        >>> output_img(img, filename="example_img.tif", window_size=(1024, 1024), show_img=True)
    """

    if show_img:
        cv2.namedWindow("Image", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
        cv2.resizeWindow("Image", window_size[0], window_size[1])
        cv2.imshow("Image", img)
    if filename is not None:
        cv2.imwrite(filename=filename, img=img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
