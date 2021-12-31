
'''******** 图片的加载 ---- 获得一个RGB三通道的矩阵数据 ********'''
import skimage.io as io
image1 = io.imread("./Example_Image/image1.jpg")
print(image1)

'''******** 图片的展示 ---- 将RGB三通道的矩阵转换成图像 ********'''
import matplotlib.pyplot as plt
plt.imshow(image1)
plt.show()

'''******** 图片的储存 ---- 图像储存格式自定（png、jpg等都可以） ********'''
io.imsave("./Example_Image/image1_new.jpg",image1)