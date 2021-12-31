'''

# 对于识别不规则的形状，可以用模板匹配来实现。模板即我们想识别检测的形状。

************ 模板匹配 ---- 代码实现 ************
import skimage.feature as feature
import numpy as np
res = feature.match_template(image,template)    image为图像，template为模板。输出一个匹配度矩阵
index = np.where(res == np.max(res))            寻找匹配度最高的点

************ 模板匹配的不足 ************
经典算法对于抗干扰能力很弱、抗泛化能力不足。在图像经过旋转、缩放、形变、遮挡、亮度等调整后很可能就难以精确匹配。

************ 高级经典算法举例 ************
SIFT、Cascade等 ---- 但基本都没有CNN好用
'''

#模板匹配
import skimage.io as io
import skimage.feature as feature
from skimage import draw
import numpy as np
import matplotlib.pyplot as plt

# 加载猫图
img=io.imread("./Example_Image/cat.jpg")
plt.imshow(img)

#制作眼睛模板
template=img[80:150,130:210,:]

#进行模板匹配
res = feature.match_template(img,template,pad_input=True,mode="constant",constant_values=0)
index = np.where(res == np.max(res))
#显示匹配度最高的点
plt.imshow(res);plt.show()
print(res)
print(index)
# 在原图中指出匹配度最高的点
h,w=draw.disk(center=(index[0][0],index[1][0]),radius=10)
draw.set_color(img,[h,w],[255,0,0])
plt.imshow(img);plt.show()


