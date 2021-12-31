
'''

# 现实多因子房价预测 #

**** 任务 ****
基于data.csv数据，建立多因子线性回归模型，与只使用面积单因子进行建模预测的结果进行对比
拓展任务：尝试以人均收入、平均房龄作为单因子的模型，思考因子与价格的关系

**** 主要任务流程 ****
1、以面积、人均收入、平均房龄分别作为单因子变量，建立单因子模型，评估模型表现，可视化线性回归预测结果
2、以面积、人均收入、平均房龄为输入变量，建立多因子模型，评估模型表现
3、预测面积=160, 人均收入=70000, 平均房龄=5的合理房价

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

#1、以面积、人均收入、平均房龄分别作为单因子变量，建立单因子模型，评估模型表现，可视化线性回归预测结果

#数据预处理
X1 = np.array(data.loc[:,'面积']).reshape(-1,1)
X2 = np.array(data.loc[:,'人均收入']).reshape(-1,1)
X3 = np.array(data.loc[:,'平均房龄']).reshape(-1,1)
y = np.array(data.loc[:,'价格']).reshape(-1,1)

#模型的建立与训练
from sklearn.linear_model import LinearRegression
model1 = LinearRegression()
model1.fit(X1,y)
model2 = LinearRegression()
model2.fit(X2,y)
model3 = LinearRegression()
model3.fit(X3,y)

#模型预测
y_predict1 = model1.predict(X1)
y_predict2 = model2.predict(X2)
y_predict3 = model3.predict(X3)

#数据可视化
fig,axes = plt.subplots(1,3,figsize=(45,15))
axes[0].scatter(data.loc[:,'面积'],data.loc[:,'价格'])
axes[0].plot(X1,y_predict1,'r')
axes[0].set_title('Price VS Size')

axes[1].scatter(data.loc[:,'人均收入'],data.loc[:,'价格'])
axes[1].plot(X2,y_predict2,'r')
axes[1].set_title('Price VS Income')

axes[2].scatter(data.loc[:,'平均房龄'],data.loc[:,'价格'])
axes[2].plot(X3,y_predict3,'r')
axes[2].set_title('Price VS House_age')
fig.savefig('result_1.png')

#模型评估
from sklearn.metrics import mean_squared_error,r2_score
MSE_1 = mean_squared_error(y,y_predict1)
R2_1 = r2_score(y,y_predict1)
MSE_2 = mean_squared_error(y,y_predict2)
R2_2 = r2_score(y,y_predict2)
MSE_3 = mean_squared_error(y,y_predict3)
R2_3 = r2_score(y,y_predict3)
print(f"面积-价格 MSE：{MSE_1}")
print(f"面积-价格 R2：{R2_1}")
print(f"人均收入-价格 MSE：{MSE_2}")
print(f"人均收入-价格 R2：{R2_2}")
print(f"平均房龄-价格 MSE：{MSE_3}")
print(f"平均房龄-价格 R2：{R2_3}")


#2、以面积、人均收入、平均房龄为输入变量，建立多因子模型，评估模型表现

#X y再次赋值
X = data.drop(['价格'],axis=1)
y = data.loc[:,'价格']
X.head()

#建立多因子回归模型 并且训练
model_multi = LinearRegression()
model_multi.fit(X,y)

#多因子模型预测
y_predict_multi = model_multi.predict(X)

#可视化预测结果 ———— 由于多因子模型包含三个变量，实际上是三维的不能绘制二维图像，因此可视化绘制实际值和预测值
fig2 = plt.figure(figsize=(15,15))
plt.scatter(y,y_predict_multi)
plt.xlabel('real price')
plt.ylabel('prdicted price')
plt.savefig('result_2.png')

#预测面积=160, 人均收入=70000, 平均房龄=5的合理房价
X_test = np.array([[160,70000,5]])      #二维数组形式
y_test_predict = model_multi.predict(X_test)
print(y_test_predict)

#多因子模型评估
MSE_multi = mean_squared_error(y,y_predict_multi)
R2_multi = r2_score(y,y_predict_multi)
print(f"多因子模型 MSE：{MSE_multi}")
print(f"多因子模型 R2：{R2_multi}")

'''

线性回归房价实战summary：
1、通过搭建线性回归模型，实现单因子的房屋价格预测；
2、在单因子模型效果不好的情况下，通过考虑更多的因子，建立了多因子模型；
3、多因子模型达到了更好的预测效果，r2分数从单因子的0.1提高到了0.55；
4、实现了预测结果的可视化，直观对比预测价格与实际价格的差异。

'''