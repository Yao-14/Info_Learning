
'''

# 基于面积的单因子房价预测 #

**** 任务 ****
基于课程中的房价预测案例与data.csv数据，建立单因子线性回归模型，预测面积100平方米的房子售价100万是否值得投资：

**** 线性回归主要流程 ****
1、完成数据加载与可视化
2、进行数据预处理: X、y赋值、格式转化、维度确认等
3、建立线性回归模型，训练模型
4、模型预测结果
5、可视化结果，并评估模型表现

'''


#数据加载
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
data = pd.read_csv('data.csv')

#数据预处理
##赋值
X = data.loc[:,'面积']
y = data.loc[:,'房价']
##格式转换成数组
X = np.array(X)
y = np.array(y)
##维度确认（转换为矩阵形式，不能为向量）
X = X.reshape(-1,1)
y = y.reshape(-1,1)

#建立模型（线性回归模型，线性回归模型即 y = ax + b 形式）
from sklearn.linear_model import LinearRegression
model = LinearRegression()

#模型训练
model.fit(X,y)

#第一种结果预测方法 ———— 通过获取线性回归模型的参数a b
a = model.coef_[0][0]      # model.coef_获得的是一个二维数组
b = model.intercept_[0]    # model.intercept_获得的是一个一维数组
y_predict =a*X+b
print(f"线性回归模型为：y = f(x) = {a}x + {b}")
#第二种预测方法 ———— 通过 predict 函数
y_predict2 = model.predict(X)

#测试样本X_test = 100，计算y
X_test = np.array([[100]])      #二维数组形式
y_test_predict = model.predict(X_test)

#数据可视化
fig2 = plt.figure()
plt.scatter(X,y)
plt.plot(X,y_predict,label='y_predict')
plt.xlabel('size(x)')
plt.ylabel('price(y)')
plt.legend()
plt.savefig('result.png')

#模型评估 ———— 通过计算损失函数的大小 (损失函数J = 1/2m * sum([y'i - yi]^2, 1 <= i <= m)
from sklearn.metrics import mean_squared_error,r2_score
MSE = mean_squared_error(y,y_predict)   # MSE指y与y'的均方差值，结果为损失函数的两倍。MSE越小，模型越好。
R2 = r2_score(y,y_predict)              # R2 = 1 - MSE/方差。R2越接近1，模型越好。
                                        # 当R2 = 1时，完美拟合。
                                        # 当R2 < 0，代表模型非常非常差，完全不可用。
                                        # 当R2 = 0，代表模型是一个常数，比如 y = 1。
print(f"MSE：{MSE}")
print(f"R2：{R2}")

'''

单因子线性回归房价实战summary：
1、完成了数据的预处理、格式转化、维度确认等步骤；
2、通过搭建线性回归模型，实现单因子的房屋价格预测；
3、通过引入MSE、R2分数完成了模型表现评估，并且实现了结果的可视化；

'''