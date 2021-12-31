'''
************ 图像滤波简介 ************
图像预处理之图像滤波：指通过卷积方法运用特定手段消除图像中混入的噪音，为图像识别抽取出图像特征。————两个作用分别依赖于平滑滤波和边缘检测

************ 边缘检测 ———— 图像识别抽取出图像特征 ************
边缘检测实现方法1：使用Roberts算子进行卷积
边缘检测实现方法2：使用Prewitt算子进行卷积（包括水平、垂直、对角线三种）
边缘检测实现方法3：使用Sobel算子进行卷积（包括水平、垂直、对角线三种）
边缘检测实现方法4：使用Canny算子 ---- 具体操作如下：
                                      用高斯滤波平滑图像
                                      用sobel等梯度算子计算梯度幅值和方向
                                      对梯度幅值进行非极大值抑制
                                      用双阈值算法检测和连接边缘

************ 边缘检测 ———— 不同算子效果比较 ************
Roberts     擅长低噪音和梯度较大的图像，但是边缘提取比较粗，定位不是很准
Prewitt     对于灰度渐变和噪音较多的图像处理较好
Sobel       对于灰度渐变和噪音较多的图像处理较好
Laplcian    对于阶跃性边缘点比较好，但是对噪音敏感，容易产生不连续的检测边缘
Log         善于判断边缘在图像明区还是暗区，对噪音比较敏感
Canny       抗噪音好对于弱边缘检测较好 ———— 好，第一选择

************ 边缘检测代码实现 ************
from skimage import filters
from skimage import feature
filters.roberts(img_gray)       Roberts算子进行边缘检测
filters.prewitt_h(img_gray)     Prewitt水平算子进行边缘检测
filters.prewitt_v(img_gray)     Prewitt垂直算子进行边缘检测
filters.prewitt(img_gray)       Prewitt算子进行边缘检测
filters.sobel_h(img_gray)       Sobel水平算子进行边缘检测
filters.sobel_v(img_gray)       Sobel垂直算子进行边缘检测
filters.sobel(img_gray)         Sobel算子进行边缘检测
feature.canny(img_gray,sigma)   Canny算子进行边缘检测

'''

#边缘检测滤波

import skimage.io as io
import skimage.filters as filters
import skimage.feature as feature
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# 导入图像
image = io.imread("./Example_Image/4.jpg")
# 将图像转化成灰度图
img_gray= rgb2gray(image)

'''******** robert 算子 ********'''
# 使用robert算子进行滤波
img_e=filters.roberts(img_gray)
plt.imshow(img_e);plt.show()

'''******** prewitt 算子 ********'''
# 使用 prewitt 算子进行滤波
img_e=filters.prewitt(img_gray)
# 使用 prewitt 算子中独立的水平算子进行滤波
img_e1=filters.prewitt_h(img_gray)
# 使用 prewitt 算子中独立的垂直算子进行滤波
img_e2=filters.prewitt_v(img_gray)
#检测结果展示
plt.figure("prewitt",figsize=(15,5),dpi=300)
plt.subplot(131);plt.imshow(img_e,plt.cm.gray) ;plt.title('prewitt')
plt.subplot(132);plt.imshow(img_e1,plt.cm.gray);plt.title('prewitt horizontal')
plt.subplot(133);plt.imshow(img_e2,plt.cm.gray);plt.title('prewitt vertical')
plt.show()



'''******** sobel 算子 ********'''
# 使用 sobel 算子
img_e=filters.sobel(img_gray)
# 使用 sobel 水平算子
img_e1=filters.sobel_h(img_gray)
# 使用 sobel 垂直算子
img_e2=filters.sobel_v(img_gray)
#结果展示
plt.figure("sobel",figsize=(15,5),dpi=300)
plt.subplot(131);plt.imshow(img_e); plt.title('sobel')
plt.subplot(132);plt.imshow(img_e1);plt.title('sobel horizontal')
plt.subplot(133);plt.imshow(img_e2);plt.title('sobel vertical')
plt.show()

'''******** canny 算子 ********'''
#使用canny算子进行检测
img_e=feature.canny(img_gray,sigma=2)
plt.imshow(img_e);plt.show()