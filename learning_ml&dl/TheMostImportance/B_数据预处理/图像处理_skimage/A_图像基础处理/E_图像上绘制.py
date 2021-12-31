
'''******** 图片的加载 ---- 获得一个RGB三通道的矩阵数据 ********'''
import skimage.io as io
image1 = io.imread("./Example_Image/image1.jpg")

'''******** 图片上绘制的实现方法1 ---- 通过手动改变某些像素点的数据而改变其颜色，从而起到绘制的效果 ********'''
import matplotlib.pyplot as plt
# 将图像的某一区域变为红色（即将R通道数据转化为255，其余2通道数据转化为0）
image1[100:150,100:150,0] = 255
image1[100:150,100:150,1] = 0
image1[100:150,100:150,2] = 0
plt.imshow(image1);plt.show()

'''******** 图片上绘制的实现方法2 ---- 通过skimage内置函数 draw 实现绘制 ********'''
from skimage import draw

# 通过draw.line()绘制直线 （r0=直线起始点y轴坐标,c0=直线起始点x轴坐标,r1=直线终点y轴坐标,c1=直线终点x轴坐标）
h,w = draw.line(r0=100,c0=200,r1=150,c1=250) # 通过draw.line()获得该直线上的所有像素点的位置信息
image1[h,w,0] = 255
image1[h,w,1] = 0
image1[h,w,2] = 0
plt.imshow(image1);plt.show()

# 通过draw.set_color() 修改图片特定位置的颜色
draw.set_color(image1,[h,w],[0,0,255])
plt.imshow(image1);plt.show()

# 通过draw.disk()绘制实心圆(center=坐标,radius=半径
h,w=draw.disk(center=(100,100),radius=30)
draw.set_color(image1,[h,w],[255,100,0])
plt.imshow(image1);plt.show()

# 通过draw.circle()绘制空心圆(r=y轴坐标,c=x轴坐标,radius=半径
h,w=draw.circle_perimeter(200,200,30)
draw.set_color(image1,[h,w],[255,0,0])
plt.imshow(image1);plt.show()