'''

# 逻辑回归实现产品分类 #

**** 任务 ****
基于课程中的线性二分类案例与data数据，建立逻辑回归模型，计算并绘制边界曲线，并预测x1=1, x2=10数据点属于什么类别。

**** 主要任务流程 ****
1、基于task1_data.csv数据，建立逻辑回归模型，评估模型表现；
2、预测x1=1, x2=10时，改产品是良品（ok）还是次品
3、获取边界函数参数、绘制边界函数

**** 逻辑回归主要流程 ****
1、数据加载并可视化，判断是线性逻辑回归还是非线性逻辑回归
2、数据预处理
3、建立逻辑回归模型，训练模型
4、模型预测结果
5、评估模型表现
6、获取边界函数参数、绘制边界函数

**** 边界函数 ****
线性边界函数： theta_0 + theta_1 X_1 + theta_2 X_2 = 0
'''

#数据加载及可视化
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
data = pd.read_csv('data.csv')
mask = data.loc[:,'y']==1   #建立筛选良品、次品的变量mask
plt.figure()
ok = plt.scatter(data.loc[:,'尺寸1'][mask],data.loc[:,'尺寸2'][mask])
ng = plt.scatter(data.loc[:,'尺寸1'][~mask],data.loc[:,'尺寸2'][~mask])
plt.xlabel('size1');plt.ylabel('size2');plt.legend((ok,ng),('ok','ng'))
plt.savefig('pre.png')
#通过可视化结果可知两个类别分隔线近似于直线，选择线性逻辑回归，即边界函数 $\theta_0 + \theta_1 X_1 + \theta_2 X_2 = 0$

#数据预处理
X = data.drop(['y'],axis=1)
y = data.loc[:,'y']

#模型建立与训练
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X,y)

#模型预测
y_predict = model.predict(X)

#模型评估
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y,y_predict) # accuracy指准确度，即类别正确预测的比例，accuracy= 正确预测样本数量/总样本数量。准确度越接近1，模型越好。

#测试样本预测
X_test = np.array([[1,10]])
y_test_p = model.predict(X_test)
print('ok' if y_test_p==1 else 'ng')

#获取边界函数的参数
theta0 = model.intercept_[0]
theta1, theta2 = model.coef_[0][0],model.coef_[0][1]

#计算边界函数上对应的X2
X1 = data.loc[:,'尺寸1']
X2_new = -(theta0+theta1*X1)/theta2

plt.figure()
ok = plt.scatter(data.loc[:,'尺寸1'][mask],data.loc[:,'尺寸2'][mask])
ng = plt.scatter(data.loc[:,'尺寸1'][~mask],data.loc[:,'尺寸2'][~mask])
plt.plot(X1,X2_new)
plt.title('chip size1-size2')
plt.xlabel('size1')
plt.ylabel('size2')
plt.legend((ok,ng),('ok','ng'))
plt.savefig('result.png')

'''

逻辑回归实现产品分类实战summary：
1、通过搭建线性边界逻辑回归模型，实现了产品良品、次品分类预测；
2、引入准确率作为评估指标、结合结果可视化完成了模型评估；
3、调用predict方法对新的样本做了预测，发现其为NG次品类别；
4、实现了分类边界的可视化，帮助理解分类任务的原理与过程。
参考链接：
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

'''