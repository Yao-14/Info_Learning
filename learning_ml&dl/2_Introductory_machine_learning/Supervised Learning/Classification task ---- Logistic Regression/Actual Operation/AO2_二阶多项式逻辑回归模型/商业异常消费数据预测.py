'''
# 商业异常消费数据预测 #

**** 任务 ****
基于task2_data.csv数据，建立二阶多项式逻辑回归模型实现异常消费数据预测，与线性逻辑回归模型结果进行对比。

**** 主要任务流程 ****
1、建立线性边界的逻辑回归模型，评估模型表现；
2、建立二阶多项式边界的逻辑回归模型，对比其与线性边界的表现
3、预测pay1=80, pay2=20时对应消费是否为异常消费
4、获取边界函数参数、绘制边界函数

**** 逻辑回归主要流程 ****
1、数据加载并可视化，判断是线性逻辑回归还是非线性逻辑回归
2、数据预处理
3、建立逻辑回归模型，训练模型
4、模型预测结果
5、评估模型表现
6、获取边界函数参数、绘制边界函数

**** 边界函数 ****
线性边界函数： theta_0 + theta_1 X_1 + theta_2 X_2 = 0

二阶边界函数：theta_0 + theta_1 X_1 + theta_2 X_2+ theta_3 X_1^2 + theta_4 X_2^2 + theta_5 X_1 X_2 = 0
           a x^2 + b x + c=0: x1 = (-b+(b^2-4ac)^.5)/2a,x1 = (-b-(b^2-4ac)^.5)/2a
           ****   theta_4 X_2^2 + (theta_5 X_1+ theta_2) X_2 + (theta_0 + theta_1 X_1 + theta_3 X_1^2)=0    ****
'''

#数据加载及可视化
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
data = pd.read_csv('data.csv')
mask= data.loc[:,'y']==1
plt.figure()
abnormal = plt.scatter(data.loc[:,'pay1'][mask],data.loc[:,'pay2'][mask])
normal = plt.scatter(data.loc[:,'pay1'][~mask],data.loc[:,'pay2'][~mask])
plt.title('pay1_pay2');plt.xlabel('pay1');plt.ylabel('pay2');plt.legend((abnormal,normal),('abnormal','normal'))
plt.savefig('pre.png')

#1、建立线性边界的逻辑回归模型，评估模型表现

#数据预处理
X = data.drop(['y'],axis=1)
y = data.loc[:,'y']
#建立线性边界分类模型
from sklearn.linear_model import LogisticRegression
LR1 = LogisticRegression()
LR1.fit(X,y)
#模型预测
y_predict = LR1.predict(X)
#准确率计算
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y,y_predict)
print(accuracy)
#边界函数参数获取及可视化
theta0 = LR1.intercept_
theta1,theta2 = LR1.coef_[0][0],LR1.coef_[0][1]
X1 = data.loc[:,'pay1']
X2_new = -(theta0+theta1*X1)/theta2
plt.figure()
abnormal = plt.scatter(data.loc[:,'pay1'][mask],data.loc[:,'pay2'][mask])
normal = plt.scatter(data.loc[:,'pay1'][~mask],data.loc[:,'pay2'][~mask])
plt.plot(X1,X2_new)
plt.title('pay1_pay2');plt.xlabel('pay1');plt.ylabel('pay2');plt.legend((abnormal,normal),('abnormal','normal'))
plt.show()

#2、建立二阶多项式边界的逻辑回归模型，对比其与线性边界的表现

#数据预处理
X1 = data.loc[:,'pay1']
X2 = data.loc[:,'pay2']
#生成二次项
X1_2 = X1*X1
X2_2 = X2*X2
X1_X2 = X1*X2
#创建二次分类边界数据
X_new = {'X1':X1,'X2':X2,'X1_2':X1_2,'X2_2':X2_2,'X1_X2':X1_X2}
X_new = pd.DataFrame(X_new)

#建立二阶多项式边界分类模型
LR2 = LogisticRegression()
LR2.fit(X_new,y)

#模型预测
y2_predict = LR2.predict(X_new)

#准确率
accuracy2 = accuracy_score(y,y2_predict)
print(accuracy2)

#边界函数参数获取及可视化————二阶多项式边界函数 theta_4 X_2^2 + (theta_5 X_1+ theta_2) X_2 + (theta_0 + theta_1 X_1 + theta_3 X_1^2)=0
theta0 = LR2.intercept_
theta1,theta2,theta3,theta4,theta5 = LR2.coef_[0][0],LR2.coef_[0][1],LR2.coef_[0][2],LR2.coef_[0][3],LR2.coef_[0][4]
X1_new = X1.sort_values()
a = theta4
b = theta5*X1_new + theta2
c = theta0+theta1*X1_new+theta3*X1_new*X1_new
X2_new_2 = (-b+np.sqrt(b*b-4*a*c))/(2*a)
plt.figure()
abnormal = plt.scatter(data.loc[:,'pay1'][mask],data.loc[:,'pay2'][mask])
normal = plt.scatter(data.loc[:,'pay1'][~mask],data.loc[:,'pay2'][~mask])
plt.plot(X1_new,X2_new_2)
plt.title('pay1_pay2')
plt.xlabel('pay1')
plt.ylabel('pay2')
plt.legend((abnormal,normal),('abnormal','normal'))
plt.savefig('result.png')

#新样本预测pay1=80, pay2=20
X_test = np.array([[80,20,80*80,20*20,80*20]])
y_predict = LR2.predict(X_test)
print('abnormal' if y_predict==1 else 'normal')

'''

商业异常消费数据预测实战summary：
1、通过搭建线性边界逻辑回归模型，实现了消费者消费行为的分类预测；
2、结合准确率指标与可视化分类结果，发现线性边界分类效果不是很理想；
3、引入了二次项数据，完成二阶多项式边界的逻辑回归预测，实现分类准确率从0.8提高到0.97，模型表现提升明显
3、调用predict方法对新的样本做了预测，发现其为正常消费；
4、实现了二阶分类边界的可视化，观察其发现该边界确实可以很好的区分两类样本从而达到很好的分类效果。
参考链接：
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

'''