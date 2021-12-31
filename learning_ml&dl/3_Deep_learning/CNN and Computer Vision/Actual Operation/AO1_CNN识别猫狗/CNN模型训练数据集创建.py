'''

# CNN识别猫狗 #

**** 任务 ****
基于task1_data数据，建立cnn模型，实现猫狗识别。

**** 主要任务流程 ****
1、通过ImageDataGenerator模块，实现本地图片批量加载；
2、查看数据基本结构，可视化加载后的样本图片；
3、建模并训练模型（迭代20次），计算训练集、测试集准确率；
4、对提供的1-9猫/狗图片，进行预测

'''
''' ******** 数据加载及预处理 ********'''
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt
train_datagen = ImageDataGenerator(rescale=1. / 255)
training_set = train_datagen.flow_from_directory('./task1_data/training_set', target_size=(50, 50), batch_size=32, class_mode='binary')
# 查看数据类型
print(type(training_set))
# 每个批次的样本数量
print(training_set.batch_size)
# 加载的图片名称
print(training_set.filenames)
# 确认标签
print(training_set.class_indices)
# training-set[][][] 第一个为第几个批次；第二个为确定输入X还是y；第三个用于确定第几个样本
print(training_set[0][1])
# 第一个批次第一个样本的输入数据，并可视化第一个批次第一张图片
print(training_set[0][0][0, :, :, :])
fig1 = plt.figure()
plt.imshow(training_set[0][0][0, :, :, :])
plt.show()
# 加载后按批次存放的每个样本对应的索引号
print(training_set.index_array)
# 获取文件名称
print(training_set.filenames[2384])

''' ******** 建立CNN模型和训练模型 ********'''
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense
cnn_model = Sequential()
# 添加卷积层
cnn_model.add(Conv2D(32, (3, 3), input_shape=(50, 50, 3), activation='relu'))
# 添加池化层
cnn_model.add(MaxPool2D(pool_size=(2, 2)))
# 添加卷积层
cnn_model.add(Conv2D(32, (3, 3), activation='relu'))
# 添加池化层
cnn_model.add(MaxPool2D(pool_size=(2, 2)))
# flatten展开
cnn_model.add(Flatten())
# FC层
cnn_model.add(Dense(units=128, activation='relu'))
# 预测输出层
cnn_model.add(Dense(units=1, activation='sigmoid'))
cnn_model.summary()
# 模型配置
cnn_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# 模型训练
cnn_model.fit_generator(training_set, epochs=20)
# 训练集数据预测损失函数和准确率（前者为损失函数，后者为准确率）
J_train,accuracy_train = cnn_model.evaluate(training_set)
print(J_train,accuracy_train)
# 模型存储
cnn_model.save('task1_model_1.h5')

'''

CNN识别猫狗实战summary：


1、通过搭建CNN模型，实现了对复杂图像的自动识别分类；
2、掌握了新的图片批量加载方法（ImageDataGenerator模块），实现本地图片批量加载与查看；
3、更熟练的掌握了keras的sequence结构，在基本的mlp结构基础上嵌入卷积、池化层；
4、实现了新图片的分类识别

图像预处理参考资料：https: // keras.io / preprocessing / image /

'''