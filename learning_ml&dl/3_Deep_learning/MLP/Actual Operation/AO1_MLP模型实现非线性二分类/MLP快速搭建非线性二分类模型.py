'''

# MLP快速搭建非线性二分类模型 #

**** 任务 ****
基于task1_data数据，建立mlp模型，实现非线性边界二分类。

**** 模型结构 ****
模型结构：一层隐藏层，25个神经元，激活函数：sigmoid

**** 主要任务流程 ****
1、数据分离: test_size = 0.2, random_state = 0；
2、建模并训练模型（迭代1000次），计算训练集、测试集准确率；
3、可视化预测结果
4、继续迭代6000次，重复步骤2 - 3
5、迭代1 - 10000次（500为间隔），查看迭代过程中的变化(可视化结果、准确率）


拓展任务：建立实现非线性边界分类的逻辑回归模型，尝试完成课程数据分类，并和MLP模型结果进行对比
CSDN线上实验平台：http://labs.csdn.net/

**** MLP模型搭建主要流程 ****
1、数据加载并可视化
2、数据预处理（数据分离: 测试数值占总样本的20%，训练数据占总样本的80%）
3、建立模型，训练模型
4、模型预测结果
5、结果展示及评估模型表现

'''

''' ******** 数据加载 ********'''
import pandas as pd
import numpy as np
data = pd.read_csv('task1_data.csv')
X = data.drop(['y'], axis=1)
y = data.loc[:, 'y']
# 原始数据的数据可视化
from matplotlib import pyplot as plt
fig1 = plt.figure(figsize=(5, 5))
label1 = plt.scatter(X.loc[:, 'x1'][y == 1], X.loc[:, 'x2'][y == 1])
label0 = plt.scatter(X.loc[:, 'x1'][y == 0], X.loc[:, 'x2'][y == 0])
plt.legend((label1, label0), ('label1', 'label0'));plt.xlabel('x1');plt.ylabel('x2');plt.title('raw data')
plt.show()

''' ******** 数据预处理 ********'''
# 数据分类（将总样本分为测试数据和训练数据: 测试数据占总样本的20%，训练数据占总样本的80%）
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print(X_train.shape, X_test.shape, X.shape)

''' ******** 建立模型和训练模型 ********'''
# 建立mlp模型
from keras.models import Sequential
from keras.layers import Dense, Activation
mlp = Sequential()
mlp.add(Dense(units=25, input_dim=2, activation='sigmoid'))
mlp.add(Dense(units=1, activation='sigmoid'))
mlp.summary()
# 模型求解参数配置
mlp.compile(optimizer='adam', loss='binary_crossentropy')
# 模型训练
mlp.fit(X_train, y_train, epochs=6000)
''' ******** 模型预测 ********'''
# 训练数据结果预测
y_train_predict=(mlp.predict(X_train) > 0.5).astype("int32")
# 测试数据结果预测
y_test_predict=(mlp.predict(X_test) > 0.5).astype("int32")

''' ******** 模型结果评估 ********'''
# 训练数据表现评估
from sklearn.metrics import accuracy_score
accuracy_train = accuracy_score(y_train, y_train_predict)
print(accuracy_train)
# 测试数据表现评估
accuracy_test = accuracy_score(y_test, y_test_predict)
print(accuracy_test)

''' ******** 模型结果可视化 ********'''
xx, yy = np.meshgrid(np.arange(0, 100, 1), np.arange(0, 100, 1))
x_range = np.c_[xx.ravel(), yy.ravel()]
y_range_predict=(mlp.predict(x_range) > 0.5).astype("int32")
y_range_predict_form = pd.Series(i for i in y_range_predict)

fig = plt.figure(figsize=(5, 5))
label1_predict = plt.scatter(x_range[:, 0][y_range_predict_form == 1], x_range[:, 1][y_range_predict_form == 1])
label0_predict = plt.scatter(x_range[:, 0][y_range_predict_form == 0], x_range[:, 1][y_range_predict_form == 0])
label1 = plt.scatter(X.loc[:, 'x1'][y == 1], X.loc[:, 'x2'][y == 1])
label0 = plt.scatter(X.loc[:, 'x1'][y == 0], X.loc[:, 'x2'][y == 0])
plt.legend((label1, label0, label1_predict, label0_predict), ('label1', 'label0', 'label1_predict', 'label0_predict'))
plt.xlabel('x1')
plt.ylabel('x2')
fig.savefig('result.png', dpi=500, bbox_inches='tight')

'''

MLP快速搭建非线性二分类模型实战summary：

1、在不增加高阶特征项的情况下，通过建立mlp模型，实现了非线性二分类任务；
2、掌握了mlp模型的建立、配置与训练方法，完成了数据分离、模型训练、预测与评估任务；
3、熟悉了mlp分类的预测数据格式，并实现格式转换；
4、通过修改迭代次数，实现了mlp训练过程结果的可视化，帮助更好地理解模型训练过程、

'''