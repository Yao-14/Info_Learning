'''

# mlp模型迁移数据预测 #

**** 任务 ****
任务：基于task1_data1、task1_data2数据，建立mlp模型，并实现模型迁移学习：

**** 主要任务流程 ****
1、基于data1完成基本的数据加载、可视化工作；
2、建立mlp模型，epochs分别为500、1000、1500、2500次，可视化数据预测结果
3、模型存储为model1及加载为model2
4、基于data2，对model2进行迁移训练，epochs=20、100，可视化模型对数据的预测结果
拓展任务：逐步增加epochs，生成预测结果gif，查看迁移学习过程

**** 模型结构 ****
两个隐藏层，每层50神经元（激活函数relu），输出层激活函数linear

'''

'''**** 数据加载 ****'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
data1 = pd.read_csv('task1_data1.csv')
X = data1.loc[:,'x']
y = data1.loc[:,'y']
plt.figure();plt.scatter(X,y)
plt.title('y vs x data1');plt.xlabel('x');plt.ylabel('y')
plt.show()

'''**** 数据预处理 ****'''
#维度确认
X = np.array(X).reshape(-1,1)

'''**** 模型建立及模型训练 ****'''
#建立模型
from keras.models import Sequential
from keras.layers import Dense
#创建模型
model1 = Sequential()
#添加隐藏层
model1.add(Dense(units=50, input_dim=1, activation='relu'))
model1.add(Dense(units=50,activation='relu'))
#输出层
model1.add(Dense(units=1,activation='linear'))
model1.summary()
#参数配置
model1.compile(optimizer='adam',loss='mean_squared_error')
#模型训练
model1.fit(X,y,epochs=2500)

'''**** 模型结果预测评估及可视化 ****'''
from sklearn.metrics import r2_score
#模型预测与表现评估（R2)
y_predict = model1.predict(X)
r2 = r2_score(y,y_predict);print(r2)
#模型预测结果可视化
plt.figure();plt.scatter(X,y,label='raw data');plt.scatter(X,y_predict,label='predict result')
plt.title('y vs x data1');plt.xlabel('x');plt.ylabel('y')
plt.legend();plt.show()
'''
#模型存储
import joblib
joblib.dump(model1,'model1.m')
#读取模型
model2 = joblib.load('model1.m')

'''
'''**** 迁移学习 ****'''
model2 = model1
model2.summary()
#数据加载
data2 = pd.read_csv('task1_data2.csv')
x_new =data2.loc[:,'x']
y_new = data2.loc[:,'y']
#x_new维度确认
x_new = np.array(x_new).reshape(-1,1)
#迁移学习前模型预测
y_new_predict = model2.predict(x_new)
r2_new = r2_score(y_new,y_new_predict)
print(r2_new)
plt.figure();plt.scatter(X,y,label='raw data1');plt.scatter(x_new,y_new,label='raw data2');plt.plot(x_new,y_new_predict,label='predict result data1',c='r')
plt.title('y vs x data1');plt.xlabel('x');plt.ylabel('y')
plt.legend();plt.show()

#模型迁移学习
model2.fit(x_new,y_new,epochs=80)
y_new_predict = model2.predict(x_new)
r2_new = r2_score(y_new,y_new_predict)
print(r2_new)
fig2 = plt.figure()
plt.scatter(X,y,label='raw data1')
plt.scatter(x_new,y_new,label='raw data2')

plt.plot(x_new,y_new_predict,label='predict result data2',c='r')
plt.title('y vs x data1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


'''

mlp模型迁移数据预测实战summary：

1、基于新数据与已有模型，实现了模型的迁移学习，对新数据达到了很好的拟合效果；
2、通过建立mlp模型，很好的完成了非线性回归分析；
3、掌握了mlp模型存储与加载的方法；
4、在数据分布规律类似的情况下，采用迁移学习可以快速寻找到数据规律，减少练迭代次数、缩短训练时间

'''