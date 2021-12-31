'''
# 朴素贝叶斯预测学生录取及奖学金情况实战task #

**** 任务 ****
基于task2_data数据，建立朴素贝叶斯模型预测学生申请结果

**** 主要任务流程 ****
1、计算模型对训练数据各样本预测各类别的概率及输出类别结果、计算模型准确率；
2、观察测试样本数据并主观预测每个样本的结果，然后结合模型计算对应类别概率、与结果，将两个结果进行对比
3、将测试样本数据、预测概率、结果以csv格式存储到本地

**** 朴素贝叶斯主要流程 ****
1、数据加载并可视化
2、数据预处理
3、建立逻辑回归模型，训练模型
4、模型预测结果
5、评估模型表现并输出数据
'''
#数据加载（此处数据以转换，将所有数据转换为数值形式）
import pandas as pd
import numpy as np
data = pd.read_csv('data.csv')
data.head()

#数据预处理
X = data.drop(['y'],axis=1)
y = data.loc[:,'y']

#创建朴素贝叶斯模型并训练
from sklearn.naive_bayes import CategoricalNB
model = CategoricalNB()
#模型训练
model.fit(X,y)

#训练数据的概率预测
y_predict_prob = model.predict_proba(X)
#训练的预测
y_predict = model.predict(X)

#计算模型准确率
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y,y_predict)
print(accuracy)

#测试样本预测
X_test = np.array([[2,1,1,1,1],[2,1,1,1,0],[2,1,1,0,0],[2,1,0,0,0],[2,0,0,0,0]])
y_test_predict_prob = model.predict_proba(X_test)
y_test_predict = model.predict(X_test)

#数据输出
test_data_result = np.concatenate((X_test,y_test_predict_prob,y_test_predict.reshape(5,1)),axis=1)
test_data_result = pd.DataFrame(test_data_result)
test_data_result.columns = ['score','school','award','gender','english','p0','p1','p2','y_test_predict']
test_data_result.to_csv('test_data_result.csv')
print(test_data_result)
'''

朴素贝叶斯预测学生录取及奖学金情况实战summary：

1、通过建立朴素贝叶斯模型，实现了预测申请者是否能拿到录取及获得奖学金，模型准确率0.68；
2、通过输出个样本不同结果的概率，为主观预测结果提供了依据，实现了申请者条件变化时结果变化的量化分析；
3、掌握了结果存储方法，方便未来进行结果分析

核心算法参考链接：https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html

'''