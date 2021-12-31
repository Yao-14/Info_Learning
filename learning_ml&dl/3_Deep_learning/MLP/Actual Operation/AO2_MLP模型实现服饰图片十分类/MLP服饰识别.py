'''

# MLP服饰识别 #

**** 任务 ****
基于fashion_mnist数据集，建立mlp模型，实现服饰图片十分类task

**** 模型结构 ****
两层隐藏层（激活函数：relu），分别有392、196个神经元；输出层10类，激活函数softmax

**** 主要任务流程 ****
1、实现图像数据加载、可视化
2、进行数据预处理：维度转化，归一化、输出结果格式转化
3、建立mlp模型，进行模型训练与预测，计算模型在训练、测试数据集的准确率
4、选取一个测试样本，预测其类别
5、选取测试集中9个样本，分别预测其类别

**** MLP模型搭建主要流程 ****
1、数据加载并可视化
2、数据预处理（数据分离: 测试数值占总样本的20%，训练数据占总样本的80%）
3、建立模型，训练模型
4、模型预测结果
5、结果展示及评估模型表现

'''

''' ******** 数据加载 ********'''
import numpy as np
from matplotlib import pyplot as plt
import gzip

def load_fm_data(x_tr_p,y_tr_p,x_te_p,y_te_p):

    with gzip.open(y_tr_p, 'rb') as lbpath:
        y_train = np.frombuffer(lbpath.read(), np.uint8, offset=8)

    with gzip.open(x_tr_p, 'rb') as imgpath:
        x_train = np.frombuffer(imgpath.read(), np.uint8, offset=16).reshape(len(y_train), 28, 28)

    with gzip.open(y_te_p, 'rb') as lbpath:
        y_test = np.frombuffer(lbpath.read(), np.uint8, offset=8)

    with gzip.open(x_te_p, 'rb') as imgpath:
        x_test = np.frombuffer(
            imgpath.read(), np.uint8, offset=16).reshape(len(y_test), 28, 28)

    return (x_train, y_train), (x_test, y_test)

(X_train,y_train),(X_test,y_test) = load_fm_data(x_tr_p = 'train-images-idx3-ubyte.gz',
                                                 y_tr_p = 'train-labels-idx1-ubyte.gz',
                                                 x_te_p = 't10k-images-idx3-ubyte.gz',
                                                 y_te_p = 't10k-labels-idx1-ubyte.gz')
# 原始数据的数据可视化
img1 = X_train[0]
fig1 = plt.figure(figsize=(3,3))
plt.imshow(img1)
plt.title('raw img 1')
plt.show()

''' ******** 数据预处理 ********'''
feature_size = img1.shape[0]*img1.shape[1]
X_train_format = X_train.reshape(X_train.shape[0],feature_size)
X_test_format = X_test.reshape(X_test.shape[0],feature_size)

# 数据的归一化处理
X_train_normal = X_train_format/255
X_test_normal = X_test_format/255

# 输出结果的数据预处理
from tensorflow.keras.utils import to_categorical
y_train_format = to_categorical(y_train)
y_test_format = to_categorical(y_test)

''' ******** 建立模型和训练模型 ********'''
from keras.models import Sequential
from keras.layers import Dense, Activation
mlp = Sequential()
mlp.add(Dense(units = 392, input_dim = 784, activation='relu'))
mlp.add(Dense(units = 196, activation='relu'))
mlp.add(Dense(units=10, activation='softmax'))
mlp.summary()
# 模型求解参数配置
mlp.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['categorical_accuracy'])
# 模型训练
mlp.fit(X_train_normal, y_train_format, epochs=10)

''' ******** 模型预测 ********'''
# 训练数据结果预测
y_train_predict = np.argmax(mlp.predict(X_train_format),axis=1)
y_test_predict = np.argmax(mlp.predict(X_test_normal),axis=1)
print(y_train_predict[0:10])
print(type(y_train_predict))

''' ******** 模型结果评估 ********'''
from sklearn.metrics import accuracy_score
# 训练数据表现评估
accuracy_train = accuracy_score(y_train,y_train_predict)
print(accuracy_train)
# 测试数据表现评估
accuracy_test = accuracy_score(y_test,y_test_predict)
print(accuracy_test)

''' ******** 模型结果可视化 ********'''
font2 = {'family': 'SimHei'}
label_dict={0:'T shirt',1:'裤子',2:'套头衫',3:'裙子',4:'外套 ',5:'凉鞋',6:'衬衫',7:'运动鞋',8:'包 ',9:'踝靴'}
img1 = X_train[100]
fig2 = plt.figure(figsize=(3,3))
plt.imshow(img1)
plt.title('predict:{}'.format(label_dict[y_train_predict[100]]),font2)
plt.show()

a = [i for i in range(1,10)]
fig4 = plt.figure(figsize=(8,8))
for i in a:
    plt.subplot(3,3,i)
    plt.imshow(X_test[i])
    plt.title('predict:{}'.format(label_dict[y_test_predict[i]]),font2)
    plt.show()

'''

Fashion_mnist图形分类实战summary：

1、通过建立mlp模型，实现了基于10种类别的服饰图片自动识别分类；
2、完成了图像数据的加载、可视化
3、对mlp模型的输入、输出数据格式有了更深的认识，完成了数据预处理与格式转换
4、建立了结构更为复杂的mlp模型，完成了预测及表现评估

fashion_mnist数据集地址：https://github.com/zalandoresearch/fashion-mnist

'''