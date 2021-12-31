'''

# RNN预测股价 #

**** 任务 ****
任务：基于task1_data数据，建立rnn模型，使用收盘价格预测贵州茅台次日收盘股价。

**** 主要任务流程 ****
1、完成基本的数据加载、可视化工作；
2、数据预处理：将数据转化为符合RNN模型输入要求的数据；
3、建立RNN模型并训练模型，计算训练集、测试集模型预测r2分数；
4、可视化预测表现；
5、将测试数据预测结果保存到本地csv文件

**** 模型结构 ****
单层RNN，输出有5个神经元。每次使用前10个数据预测第11个数据

'''

''' ******** 数据加载 ********'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
data_train = pd.read_csv('task1_data_train.csv')
#获取收盘价格并可视化
price_close = data_train.loc[:,'close']
plt.figure();plt.plot(price_close);plt.title('gzmt price close');plt.xlabel('time series');plt.ylabel('price');plt.show()

''' ******** 数据预处理 ********'''
#数据归一化————减少数据量级差距过大带来的误差
price_n = price_close/max(price_close)

#数据序列提取方法
def extract_data(data,time_step=10):
    X = []
    y = []
    for i in range(len(data)-time_step):
        X.append([a for a in data[i:i+time_step]])
        y.append(data[i+time_step])
    X = np.array(X)
    X = X.reshape(X.shape[0],X.shape[1],1)
    y = np.array(y)
    return X,y

#股票价格数据处理
time_step = 10
X,y = extract_data(price_n,time_step)

''' ******** 模型建立及模型训练 ********'''
#建立模型
from keras.models import Sequential
from keras.layers import Dense, SimpleRNN
model = Sequential()
#添加RNN层
model.add(SimpleRNN(units=5,input_shape=(10,1),activation='relu'))
#输出层
model.add(Dense(units=1,activation='linear'))
model.summary()
#模型配置
model.compile(optimizer='adam',loss='mean_squared_error')
#模型训练
model.fit(X,y,batch_size=30,epochs=200)

''' ******** 模型结果预测评估 ********'''
from sklearn.metrics import r2_score
y_train_predict = model.predict(X)
y_train_predict = y_train_predict*max(price_close)
y = [i*max(price_close) for i in y]
print(y_train_predict,y)
r2_train = r2_score(y,y_train_predict)
print(r2_train)

''' ******** 模型预测结果可视化 ********'''
plt.figure()
plt.plot(y,label='real price')
plt.plot(y_train_predict,label='predict price')
plt.title('gzmt price close')
plt.xlabel('time series')
plt.ylabel('price')
plt.legend()
plt.show()

#有的小伙伴训练一次以后发现预测出来的结果不理想，很可能是模型进行初始化的时候选取的随机系数不合适，导致梯度下降搜索时遇到了局部极小值
#解决办法：尝试再次建立模型并训练
#多层感知机结构在进行模型求解时，会给定一组随机的初始化权重系数，这种情况是正常的。通常我们可以观察损失函数是否在变小来发现模型求解是否正常

#测试集数据
data_test = pd.read_csv('task1_data_test.csv')
data_test.head()
price_test = data_test.loc[:,'close']
price_test.head()
#归一化
price_test_n = price_test/max(price_close)
print(price_test_n)

#测试数据的序列提取
X_test, y_test = extract_data(price_test_n,time_step)
print(X_test.shape,len(y_test))

#测试数据的1预测
y_test_predict = model.predict(X_test)
y_test_predict = y_test_predict*max(price_close)
print(y_test_predict)
y_test = [i*max(price_close) for i in y_test]
print(y_test)
#r2
r2_test = r2_score(y_test,y_test_predict)
print(r2_test)
#数据可视化
plt.figure()
plt.plot(y_test,label='real price')
plt.plot(y_test_predict,label='predict price')
plt.title('gzmt price close')
plt.xlabel('time series')
plt.ylabel('price')
plt.legend()
plt.show()

#数据存储
y_test_r = np.array(y_test).reshape(-1,1)
final_result = np.concatenate((y_test_r,y_test_predict),axis=1)
final_result_df = pd.DataFrame(final_result,columns=['real price','predict price'])
final_result_df.to_csv('predict_test.csv')

'''

RNN预测股价实战summary：

1、通过搭建RNN模型，完成了基于时间序列的股价预测任务；
2、在熟悉RNN模型输入数据结构的同时，实现了数字序列数据的预处理；
3、实现了数据存储，通过可视化数据局部细节了解了RNN用于股价预测的局限性：信息延迟

RNN模型参考资料：https://keras.io/zh/layers/recurrent/#rnn

'''