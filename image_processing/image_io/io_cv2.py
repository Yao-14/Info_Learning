
import cv2
import numpy as np


def read_img(
    filename: str,
    flag: int = -1,
):
    """
    Read image file.
    The image file formats that can be read include .bmp, .dib, .jpeg, .jpg, .jpe, .png, .webp, .pbm,  .pgm, .ppm, .pxm,
     .pnm, .sr, .ras, .tiff, .tif, .exr, .hdr, .pic, etc.

    Args:
        filename：Iutput image filename.
        flag：Specify the format of the desired image color space, common formats include：
            * -1 | cv2.IMREAD_UNCHANGED: Return the loaded image as is.
            * 0 | cv2.IMREAD_GRAYSCALE: Convert image to the single channel grayscale image
            * 1 | cv2.IMREAD_COLOR: Convert image to the 3 channel BGR color image.
            * 2 | cv2.IMREAD_ANYDEPTH: Return 16-bit/32-bit image when the input has the corresponding depth,
                                       otherwise convert it to 8-bit.
            * 4 | cv2.IMREAD_ANYCOLOR: The image is read in any possible color format.

    Example:
        >>> read_img("example_img.tif", flag=-1)
    """
    img = cv2.imread(filename=filename, flags=flag)

    if img is None:
        raise IOError("Could not read the image.")
    else:
        print(f"\nImage matrix size: {img.shape}.")
        print(f"\nImage matrix max value: {img.max()}.")
        print(f"\nImage matrix min valu: {img.min()}.")
        print(f"\nThe type of Image matrix values: {img.dtype}.")
        return img


def output_img(
    img: np.ndarray,
    filename: str = None,
    window_size: tuple = (1024, 1024),
    show_img: bool = True
):
    """
    Output the image matrix as a 2D image file.

    Args:
        img：Image matrix.
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
