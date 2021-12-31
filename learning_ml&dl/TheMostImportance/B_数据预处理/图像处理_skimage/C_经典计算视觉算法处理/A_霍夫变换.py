'''

# 霍夫变化主要用于识别一些规则的形状，如线、圆等。对于识别不规则的形状，可以用模板匹配来实现。

************ 霍夫变换 ---- 基本步骤 ************
霍夫变换：是一种特征检测(feature extraction)，被广泛应用在图像分析、计算机视觉以及数位影像处理。霍夫变换是用来辨别找出物件中的特征，例如：线条。
    1.选定要识别的形状的种类（线 或 圆）
    2.将直角坐标系的参数空间投影到特殊的参数空间
    3.寻找交点确定识别到的形状（通过在参数空间中累加的局部最大值来决定）

************ 霍夫变换 ---- 代码实现 ************
import skimage.transform as transform
transform.hough_line(image)             霍夫变换之线检测
transform.hough_circle(image,radius)    霍夫变换之圆检测（radius指半径大小）

'''

'''************ 霍夫变换之线检测 ************'''
from skimage import draw
import skimage.transform as transform
import numpy as np
import matplotlib.pyplot as plt
# 首先在黑色背景中绘制一条直线
img=np.zeros([100,100])
h,w=draw.line(1,1,95,95);img[h,w]=1
plt.imshow(img);plt.show()
# 进行线检测
h,theta,d=transform.hough_line(img)

plt.figure('hough_line',figsize=(16,8))
plt.subplot(121);plt.imshow(img)
plt.subplot(122);plt.imshow(np.log(1+h))
plt.show()
#显示生成的效果图
plt.figure('hough_line',figsize=(16,8))
plt.subplot(121);plt.imshow(img)
plt.subplot(122)
row1, col1 = img.shape
for _, angle, dist in zip(*transform.hough_line_peaks(h, theta, d)):
    y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
    y1 = (dist - col1 * np.cos(angle)) / np.sin(angle)
    plt.plot((0, col1), (y0, y1), '-r')
plt.axis((0,col1,row1,0))
plt.show()

'''************ 霍夫变换之圆检测 ************'''
# 首先在黑色背景中绘制图（包括线、圆、矩形）
img=np.zeros([200,200])
h,w=draw.line(1,1,10,150);img[h,w]=1
h,w=draw.circle_perimeter(150,50,30);img[h,w]=1
img[40:60,60:80]=1

#霍夫检测 ---- 生成一个三维矩阵，如（9，200，200）其中9表示使用了九种半径计算，（200，200）表示图像的大小
radii=np.arange(5,50,5) # 首先设定检测的半径范围
circle=transform.hough_circle(img,radii)
print(circle.shape)

#展示识别效果,看不同半径范围检测到的最大值
r=5 # 半径为radii的列表的第五个时是效果最佳的
plt.imshow(circle[5,:,:])
print(np.max(circle[5,:,:]))

# 设置检测到的半径， 找到最大值的位置
import skimage.feature as feature
peak=feature.peak_local_max(circle[r,:,:],num_peaks=1)
#显示生成的效果图
img2=img.copy()
cx, cy =draw.circle_perimeter(peak[0][0], peak[0][1], radii[r])
img2[cx,cy]=255
plt.figure("detect_circle",figsize=(8,8))
plt.subplot(121);plt.imshow(img)
plt.subplot(122);plt.imshow(img2)
plt.show()