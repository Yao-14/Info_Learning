'''

# 异常消费行为检测 #

**** 任务 ****
基于task2_data数据，结合PCA降维技术与逻辑回归预测检查者患病情况

**** 主要任务流程 ****
1、对原数据建立逻辑回归模型，计算模型预测准确率；
2、对数据进行标准化处理，选取glucose维度数据可视化处理后的效果；
3、进行与原数据等维度PCA，查看各主成分的方差比例；
4、保留2个主成分，可视化降维后的数据；
5、基于降维后数据建立逻辑回归模型，与原数据表现进行对比，思考结果变化原因

'''

#数据加载
import pandas as pd
import numpy as np
data = pd.read_csv('task2_data.csv')

#数据预处理
X = data.drop(['label'],axis=1)
y = data.loc[:,'label']
#print(X.shape,y.shape)

'''1、对原数据建立逻辑回归模型，计算模型预测准确率；'''
#逻辑回归模型
from sklearn.linear_model import LogisticRegression
model1 = LogisticRegression(max_iter=1000)
model1.fit(X,y)
#结果预测
y_predict = model1.predict(X)
#模型评估
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y,y_predict)
#print(accuracy)

'''2、对数据进行标准化处理，选取glucose维度数据可视化处理后的效果；'''
#数据的标准化处理————即将均值变为0，标准差变为1
from sklearn.preprocessing import StandardScaler
X_norm = StandardScaler().fit_transform(X)

#计算均值与标准差
x1_mean = X.loc[:,'glucose'].mean()
x1_norm_mean = X_norm[:,1].mean()
x1_sigma = X.loc[:,'glucose'].std()
x1_norm_sigma = X_norm[:,1].std()
#print(x1_mean,x1_sigma,x1_norm_mean,x1_norm_sigma)

from matplotlib import pyplot as plt
fig1 = plt.figure(figsize=(12,5))
fig1_1 = plt.subplot(121)
plt.hist(X.loc[:,'glucose'],bins=100)

fig1_2 = plt.subplot(122)
plt.hist(X_norm[:,1],bins=100)
plt.show()

'''3、进行与原数据等维度PCA，查看各主成分的方差比例；'''
#pca分析
from sklearn.decomposition import PCA
pca = PCA(n_components=8)   #n_components 指主成分数量，即PCA后的维度
print(X_norm[0])
print(X_norm.shape)
X_pca = pca.fit_transform(X_norm)
#计算分析后各成分的方差以及方差比例
var = pca.explained_variance_
var_ratio = pca.explained_variance_ratio_
print(sum(var_ratio))
#可视化方差比例
fig2 = plt.figure(figsize=(10,5))
plt.bar([1,2,3,4,5,6,7,8],var_ratio)
plt.show()

'''4、保留2个主成分，可视化降维后的数据；'''
#数据降维到2维
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_norm)
#print(X_pca.shape,X_norm.shape)
#计算方差比例
var_ratio2 = pca.explained_variance_ratio_
print(sum(var_ratio2))
#降维数据的可视化
fig3 = plt.figure()
plt.scatter(X_pca[:,0][y==0],X_pca[:,1][y==0],marker='x',label='negative')
plt.scatter(X_pca[:,0][y==1],X_pca[:,1][y==1],marker='*',label='positive')
plt.legend()
plt.show()
'''5、基于降维后数据建立逻辑回归模型，与原数据表现进行对比'''
#降维后的模型建立与训练
model2 = LogisticRegression()
model2.fit(X_pca,y)
#模型预测
y_predict_pca = model2.predict(X_pca)
accuracy_pca = accuracy_score(y,y_predict_pca)
#print(accuracy_pca)

'''

PCA+逻辑回归预测检查者是否患糖尿病实战summary：

1、通过对原始数据建立逻辑回归模型，实现了糖尿病人检测，并达到了92%的准确率；
2、实现了各个维度数据的标准化处理，并且通过可视化对比了处理后的数据分布变化；
3、完成了PCA分析，并通过各主成分的方差比例帮助更好的理解信息的保留情况；
4、基于PCA技术成功将数据从8D降维到2D，并将其可视化进行直观的观察；
5、对降维后数据建立新的逻辑回归模型，新模型亦达到了88%的准确率，说明我们在降维的同时保留了最主要的信息。

核心算法参考链接：https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html


'''