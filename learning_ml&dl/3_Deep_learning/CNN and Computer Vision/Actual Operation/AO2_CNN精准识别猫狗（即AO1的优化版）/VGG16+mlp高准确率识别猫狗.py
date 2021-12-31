'''

# VGG16+mlp高准确率识别猫狗 #

**** 任务 ****
基于task2_data，利用VGG16结构，提高猫狗识别的准确率：

**** 模型结构 ****
1、数据分离参数：test_size = 0.2, random_state = 0
2、mlp模型只有一个隐藏层（10个神经元）、激活函数relu

**** 主要任务流程 ****
1、对单张图片，利用VGG16提取图像特征
2、对所有图片，利用VGG16进行特征提取，并把数据分为训练数据、测试数据两部分
3、对提取特征后的数据建立mlp模型，进行模型训练，计算模型在训练、测试数据集的准确率
4、对提供的1-9猫/狗图片，进行预测，将结果与任务一的结果进行对比

'''



# load image and preprocess it with vgg16 structure
# --by flare
from keras.preprocessing.image import img_to_array, load_img
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
import numpy as np
import matplotlib.pyplot as plt

# define a method to load and preprocess the image
def modelProcess(img_path, model):
    img = load_img(img_path, target_size=(224, 224))
    img = img_to_array(img)
    x = np.expand_dims(img, axis=0)
    x = preprocess_input(x)
    x_vgg = model.predict(x)
    x_vgg = x_vgg.reshape(1, 25088)
    return x_vgg

'''**** 通过VGG16分别获得猫的特征和狗的特征 ****'''
import os
folder = "task2_data/cats"
img_path = [i for i in os.listdir(folder) if os.path.splitext(i)[1] == ".jpg"]
img_path = [folder + "//" + i for i in img_path]
model_vgg = VGG16(weights='imagenet', include_top=False)
features1 = np.zeros([len(img_path), 25088])
for i in range(len(img_path)):
    feature_i = modelProcess(img_path[i], model_vgg)
    print('preprocessed:', img_path[i])
    features1[i] = feature_i

folder = "task2_data/dogs"
dirs = os.listdir(folder)
img_path = [i for i in dirs if os.path.splitext(i)[1] == ".jpg"]
img_path = [folder + "//" + i for i in img_path]
features2 = np.zeros([len(img_path), 25088])
for i in range(len(img_path)):
    feature_i = modelProcess(img_path[i], model_vgg)
    print('preprocessed:', img_path[i])
    features2[i] = feature_i

''' ******** 数据加载 ********'''
# label the results
print(features1.shape, features2.shape)
y1 = np.zeros(300)
y2 = np.ones(300)
# generate the training data
X = np.concatenate((features1, features2), axis=0)
y = np.concatenate((y1, y2), axis=0)
y = y.reshape(-1, 1)

''' ******** 数据预处理 ********'''
# 数据分离为训练数据和测试数据
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

''' ******** 模型预测和训练 ********'''
# 建立mlp模型
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
# 隐藏层
model.add(Dense(units=10, activation='relu', input_dim=25088))
# 输出层
model.add(Dense(units=1, activation='sigmoid'))
model.summary()
# 模型求解参数配置
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# 模型训练
model.fit(X_train, y_train, epochs=50)

''' ******** 模型预测和结果评估 ********'''
from sklearn.metrics import accuracy_score
# 训练数据模型预测
y_train_predict = (model.predict(X_train) > 0.5).astype("int64")
# 训练数据预测准确率
accuracy_train = accuracy_score(y_train, y_train_predict)
print(accuracy_train)
# model保存
model.save('task2_model_1.h5')

# 测试数据预测准确率
y_test_predict = (model.predict(X_test) > 0.5).astype("int64")
accuracy_test = accuracy_score(y_test, y_test_predict)
print(accuracy_test)

''' ******** 模型结果可视化 ********'''
pic1 = './predict_data/1.png'
pic1 = load_img(pic1, target_size=(224, 224))
pic1_array = img_to_array(pic1)
pic1_array = np.expand_dims(pic1_array, axis=0)
pic1_array = preprocess_input(pic1_array)
pic1_features = model_vgg.predict(pic1_array)
pic1_features = pic1_features.reshape(1, 7 * 7 * 512)
# mlp模型预测
result = (model.predict(pic1_features) > 0.5).astype("int64")
# 1:dog； 0：cat
print('dog' if result == 1 else 'cat')
fig3 = plt.figure()
plt.imshow(pic1)
plt.show()

# 本地九张图片处理
a = [i for i in range(1, 10)]
plt.figure(figsize=(10, 10))
for i in a:
    img_name = f'./predict_data/{i}.png'

    pic1 = img_name
    pic1 = load_img(pic1, target_size=(224, 224))
    pic1_array = img_to_array(pic1)
    pic1_array = np.expand_dims(pic1_array, axis=0)
    pic1_array = preprocess_input(pic1_array)
    pic1_features = model_vgg.predict(pic1_array)
    pic1_features = pic1_features.reshape(1, 7 * 7 * 512)
    # mlp模型预测
    result =  (model.predict(pic1_features) > 0.5).astype("int32")
    # 1:dog； 0：cat
    #     print('dog' if result==1 else 'cat')
    plt.subplot(3, 3, i)
    plt.imshow(pic1)
    plt.title('predict result: dog' if result == 1 else 'predict reuslt:cat')
plt.show()


'''
VGG16 + mlp高准确率识别猫狗实战summary：

1、通过VGG16提取图像特征，再结合基本的mlp结构，实现了猫狗识别并提高了模型预测准确率；
2、掌握了利用已有的结构进行数据特征提取的方法，实现对模型的灵活应用；
3、更熟练的运用mlp模型，并将其与其他模型相结合，完成更复杂的任务；

VGG16参考资料：https://keras.io/zh/applications/#vgg16_1

'''