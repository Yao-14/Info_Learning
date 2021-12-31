'''
************ RNN模型输入数据格式（Input_shape） ************
    Input_shape = ( samples, time_steps, features ）
        samples     样本数量（可不填写）
        time_steps  序列长度，即用多少个连续样本预测一个输出
        features    每个样本的特征数

************ RNN模型输入数据格式（Input_shape）例子 ************
    假设股票数据样本有1000个，每次用10条数据预测第11条，股票数据为单维度数据，则输入数据格式shape = ( 1000, 10, 1 )

'''

# 一维列表数据转化为RNN模型输入数据格式的方法

import numpy as np
# 滑动窗口提取数据
def extract_data(data,time_steps):
    X = [] ; y = []
    for i in range(len(data)-time_steps):
        X.append([a for a in data[i:i+time_steps]]) ; y.append(data[i+time_steps])
    X = np.array(X) ; y = np.array(y)
    return X,y

data = [i for i in range(1,1001,5)]
time_steps = 10
features = 1
# 滑动窗口提取数据
X,y = extract_data(data=data,time_steps=time_steps)
# 滑动窗口数据转化为RNN模型输入数据格式
X = X.reshape(X.shape[0], X.shape[1], features)
