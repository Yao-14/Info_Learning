# 加载第一张图片并可视化
from keras.preprocessing.image import load_img, img_to_array
from matplotlib import pyplot as plt
pic1 = './task2_data/1.png'
pic1 = load_img(pic1, target_size=(224, 224))
fig1 = plt.figure()
plt.imshow(pic1)
plt.show()

''' ******** 数据预处理 ********'''
from keras.applications.vgg16 import preprocess_input
import numpy as np
# 图片格式转数组格式
pic1 = img_to_array(pic1)

x = np.expand_dims(pic1, axis=0)
x = preprocess_input(x)

''' ******** 建立模型 ********'''
# 图像核心特征提取
from keras.applications.vgg16 import VGG16
model_vgg = VGG16(weights='imagenet', include_top=False)
features = model_vgg.predict(x)
# flatten展开
features = features.reshape(1, 7 * 7 * 512)
print(features.shape)