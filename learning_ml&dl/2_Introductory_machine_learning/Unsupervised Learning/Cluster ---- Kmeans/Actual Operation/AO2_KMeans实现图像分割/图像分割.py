'''
# KMeans实现图像分割 #

**** 任务 ****
加载本地图像1.jpg，建立Kmeans模型实现图像分割。

**** 主要任务流程 ****
1、实现图像加载、可视化、维度转化，完成数据的预处理；
2、K=3建立Kmeans模型，实现图像数据聚类；
3、对聚类结果进行数据处理，展示分割后的图像；
4、尝试其他的K值（K=4、8)，对比分割效果，并思考导致结果不同的原因；
5、使用新的图片，对其实现图像分割

'''

#图像的加载
import matplotlib.pyplot as plt
from skimage import io as io
img = io.imread('image.jpg')
print(type(img));print(img.shape);print(img)

#数据预处理
img_width = img.shape[1]
img_height = img.shape[0]
img_data = img.reshape(-1,3)    #数据维度转化
X = img_data

#模型建立与训练————k3
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3,random_state=0)
model.fit(X)
#聚类结果预测
label = model.predict(X)
#结果数据的维度转化
label = label.reshape([img_height,img_width])
#后续的灰度处理
label = 1/(label+1)
#结果的可视化并存储到本地
io.imsave('result_k3.png',label)

#模型建立与训练————k4
model = KMeans(n_clusters=4,random_state=0)
model.fit(X)
label = model.predict(X)
#结果数据的维度转化
label = label.reshape([img_height,img_width])
#后续的灰度处理
label = 1/(label+1)
#结果的可视化并存储到本地
io.imsave('result_k4.png',label)

#模型建立与训练————k8
model = KMeans(n_clusters=8,random_state=0)
model.fit(X)
label = model.predict(X)
#结果数据的维度转化
label = label.reshape([img_height,img_width])
#后续的灰度处理
label = 1/(label+1)
#结果的可视化并存储到本地
io.imsave('result_k8.png',label)

'''

KMeans实现图像分割实战summary：

1、使用skimage模块，实现了图像的加载、可视化，并完成数据预处理；
2、通过建立KMeans模型，实现了图像数据的聚类；
3、对图像聚类结果进行后续处理后，完成了图像分割，并将结果可视化；
4、尝试增大K值，观察发现随着K值增大分割后的图像将展现更多的细节信息

核心算法参考链接：https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

'''