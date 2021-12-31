'''

# 少样本区分奇特草莓 #

**** 任务 ****
任务：基于task2_data//all的40张图片，建立模型有效的区分奇特草莓与普通草莓：

**** 主要任务流程 ****
1、数据增强：利用12张普通草莓图片生成更多样本
2、加载、可视化单张图片，使用VGG16提取特征
3、实现对所有样本图片的特征提取
4、建立Kmeans模型，完成图像数据聚类
5、设定样本更多的类别为普通草莓，完成结果矫正
6、使用测试图片test_data，验证模型表现
7、建立Meanshift模型，预测类别并进行结果矫正
8、引入PCA技术降低噪声数据影响，提升模型表现

'''
'''**** 数据增强 ----通过少数几张样本生成更多样本 ****'''
from keras.preprocessing.image import ImageDataGenerator
path = 'task2_data//labeled_data'
dst_path = 'task2_data//gen_data'
datagen = ImageDataGenerator(rotation_range=10, width_shift_range=0.1,height_shift_range=0.02,horizontal_flip=True,vertical_flip=True)
gen = datagen.flow_from_directory(path,target_size=(224,224),batch_size=2, save_to_dir = dst_path, save_prefix='gen',save_format='jpg')
for i in range(100):
    gen.next()

'''**** 使用VGG16实现对所有样本图片的特征提取 ****'''
#t图片加载
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input,VGG16
import numpy as np
from matplotlib import pyplot as plt
'''
单一样本特征提取
img_path = '1.jpg'
img = load_img(img_path,target_size=(224,224))
img = img_to_array(img)
#维度转化与数据预处理
img_p = np.expand_dims(img,axis=0)
img_p = preprocess_input(img_p)
#VGG16提取特征
model_vgg16 = VGG16(weights='imagenet',include_top=False)
features = model_vgg16.predict(img_p)
#特征展开 flatten
features = features.reshape(1,7*7*512)
print(features.shape)
'''
#批量图片的路径获取
import os
folder = 'task2_data//training_data'
files_name = os.listdir(folder)
img_path = [i for i in files_name if os.path.splitext(i)[1]=='.jpg']#用于存储图片路径
img_path = [folder + '//' + i for i in img_path]
print(img_path)

#VGG16特征提取方法的定义
def modelProcess(img_path,model):
    img = load_img(img_path,target_size=(224,224))
    img = img_to_array(img)
    img_p = np.expand_dims(img,axis=0)
    img_p = preprocess_input(img_p)
    img_vgg = model.predict(img_p)
    img_vgg = img_vgg.reshape(1,7*7*512)
    return img_vgg

#批量提取图片特征
features_train = np.zeros([len(img_path),7*7*512])
model_vgg16 = VGG16(weights='imagenet',include_top=False)
for i in range(len(img_path)):
    features_temp = modelProcess(img_path[i],model_vgg16)
    features_train[i] = features_temp
    print('preprocess:',img_path[i])
X = features_train

'''**** 建立Kmeans模型，完成图像数据聚类 ****'''
#kmeans模型聚类分析
from sklearn.cluster import KMeans
vgg_kmeans = KMeans(n_clusters=2,max_iter=3000)
#训练
vgg_kmeans.fit(X)
#预测
y_predict_km = vgg_kmeans.predict(X)
print(y_predict_km)
#预测结果分布统计
import pandas as pd
print(pd.value_counts(y_predict_km))

#普通草莓id
normal_strawberry_id = 1

plt.figure(figsize=(10,40))
for i in range(48):
    for j in range(5):
        img = load_img(img_path[i*5+j])
        plt.subplot(48,5,i*5+j+1)
        plt.title('n-strawberry' if y_predict_km[i*5+j]==normal_strawberry_id else 's-strawberry')
        plt.imshow(img)
        plt.axis('off')
plt.show()

''' 测试数据'''
#批量图片的路径获取
import os
folder = 'task2_data//test_data'
files_name = os.listdir(folder)
img_path = [i for i in files_name if os.path.splitext(i)[1]=='.jpg']#用于存储图片路径
img_path = [folder + '//' + i for i in img_path]

#批量提取图片特征
features_test = np.zeros([len(img_path),7*7*512])
for i in range(len(img_path)):
    features_temp = modelProcess(img_path[i],model_vgg16)
    features_test[i] = features_temp
    print('preprocess:',img_path[i])
#X_test
X_test = features_test
print(X_test.shape)
#测试数据预测
y_predict_km_test = vgg_kmeans.predict(X_test)
print(y_predict_km_test)
plt.figure(figsize=(10,10))
for i in range(3):
    for j in range(4):
        img = load_img(img_path[i*4+j])
        plt.subplot(3,4,i*4+j+1)
        plt.title('n-strawberry' if y_predict_km_test[i*4+j]==normal_strawberry_id else 's-strawberry')
        plt.imshow(img)
        plt.axis('off')
plt.show()

'''建立Meanshift模型，预测类别并进行结果矫正'''

#meanshift模型替代kmeans模型
from sklearn.cluster import MeanShift, estimate_bandwidth
#获取合适的meanshift半径
bw = estimate_bandwidth(X,n_samples=150)
vgg_ms = MeanShift(bandwidth=bw)
#模型训练
vgg_ms.fit(X)
#预测
y_predict_ms = vgg_ms.predict(X)
print(y_predict_ms)
#预测结果分布统计
print(pd.value_counts(y_predict_ms))
#普通草莓id
normal_strawberry_id = 0
#批量图片的路径获取
import os
folder = 'task2_data//training_data'
files_name = os.listdir(folder)
img_path = [i for i in files_name if os.path.splitext(i)[1]=='.jpg']#用于存储图片路径
img_path = [folder + '//' + i for i in img_path]
print(img_path)

plt.figure(figsize=(10,40))
for i in range(48):
    for j in range(5):
        img = load_img(img_path[i*5+j])
        plt.subplot(48,5,i*5+j+1)
        plt.title('n-strawberry' if y_predict_ms[i*5+j]==normal_strawberry_id else 's-strawberry')
        plt.imshow(img)
        plt.axis('off')
plt.show()
#%%

#批量图片的路径获取
import os
folder = 'task2_data//test_data'
files_name = os.listdir(folder)
img_path = [i for i in files_name if os.path.splitext(i)[1]=='.jpg']#用于存储图片路径
img_path = [folder + '//' + i for i in img_path]
print(img_path)

#测试数据预测
y_predict_ms_test = vgg_ms.predict(X_test)
print(y_predict_ms_test)
fig2 = plt.figure(figsize=(10,10))
for i in range(3):
    for j in range(4):
        img = load_img(img_path[i*4+j])
        plt.subplot(3,4,i*4+j+1)
        plt.title('n-strawberry' if y_predict_ms_test[i*4+j]==normal_strawberry_id else 's-strawberry')
        plt.imshow(img)
        plt.axis('off')
plt.show()

'''引入PCA技术降低噪声数据影响，提升模型表现'''
#PCA主成分分析
from sklearn.preprocessing import StandardScaler
standards = StandardScaler()
X_standard = standards.fit_transform(X)

from sklearn.decomposition import PCA
pca = PCA(n_components=200)
X_pca = pca.fit_transform(X_standard)
#计算降维后的方差比例
var_ratio = pca.explained_variance_ratio_
print(np.sum(var_ratio))
#创建第二个ms模型
#获取ms的半径
bw_2 = estimate_bandwidth(X_pca,n_samples=150)
print(bw_2)
vgg_pca_ms = MeanShift(bandwidth=bw_2)
vgg_pca_ms.fit(X_pca)
#模型预测
y_predict_pca_ms = vgg_pca_ms.predict(X_pca)
print(y_predict_pca_ms)
print(pd.value_counts(y_predict_pca_ms))

#普通草莓id
normal_strawberry_id = 0
#批量图片的路径获取
import os
folder = 'task2_data//training_data'
files_name = os.listdir(folder)
img_path = [i for i in files_name if os.path.splitext(i)[1]=='.jpg']#用于存储图片路径
img_path = [folder + '//' + i for i in img_path]


plt.figure(figsize=(10,40))
for i in range(48):
    for j in range(5):
        img = load_img(img_path[i*5+j])
        plt.subplot(48,5,i*5+j+1)
        plt.title('n-strawberry' if y_predict_pca_ms[i*5+j]==normal_strawberry_id else 's-strawberry')
        plt.imshow(img)
        plt.axis('off')
plt.show()

#批量图片的路径获取
import os
folder = 'task2_data//test_data'
files_name = os.listdir(folder)
img_path = [i for i in files_name if os.path.splitext(i)[1]=='.jpg']#用于存储图片路径
img_path = [folder + '//' + i for i in img_path]

X_test_standard = standards.transform(X_test)
#测试数据pca降维
X_test_pca = pca.transform(X_test_standard)
#测试数据预测
y_predict_pca_ms_test = vgg_pca_ms.predict(X_test_pca)
print(y_predict_pca_ms_test)

plt.figure(figsize=(10,10))
for i in range(3):
    for j in range(4):
        img = load_img(img_path[i*4+j])
        plt.subplot(3,4,i*4+j+1)
        plt.title('n-strawberry' if y_predict_pca_ms_test[i*4+j]==normal_strawberry_id else 's-strawberry')
        plt.imshow(img)
        plt.axis('off')
plt.show()

'''

少样本区分奇特草莓实战summary：

1、结合监督与无监督、机器学习与深度学习技术，成功搭建了混合模型，在极少数据样本的情况下有效的区分了普通草莓与奇特草莓；
2、掌握了图像数据增强方法，扩充了训练样本数据集；
3、更熟练的掌握了使用经典VGG16提取图像特征的方法；
4、完成了图像特征的批量提取；
5、在使用监督式VGG16模型完成特征提取的基础上，运用无监督聚类算法，有效地区分出了奇特草莓，寻找到了普通草莓的内在特征；
6、结合PCA技术，剔除了数据中的噪音信息、降低了模型复杂度、减少了模型训练时间，并最终提高了模型表现；

'''