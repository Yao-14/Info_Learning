import cv2


def output_img(img, filename, img_name="Image", window_size=(1000, 1000), show_img=True):
    """
    输出图像文件

    img - 图像矩阵
    filename - 要加载的图像文件名 (图像格式包括*.bmp, *.dib, *.jpeg, *.jpg, *.jpe, *.png, *.webp, *.pbm, *.pgm, *.ppm *.pxm,
                                *.pnm, *.sr, *.ras,  *.tiff, *.tif,  *.exr, *.hdr, *.pic...)
    img_name - 图像显示窗口名 (没啥用)
    window_size - 图像显示窗口大小
    show_img - 是否创建窗口展示图像

    Example:
    >> img = output_img(img, filename="img.png", img_name="Image", window_size=(1000, 1000))
    """
    if show_img:
        cv2.namedWindow(img_name, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
        cv2.resizeWindow(img_name, window_size[0], window_size[1])
        cv2.imshow(img_name, img)
    cv2.imwrite(filename=filename, img=img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
