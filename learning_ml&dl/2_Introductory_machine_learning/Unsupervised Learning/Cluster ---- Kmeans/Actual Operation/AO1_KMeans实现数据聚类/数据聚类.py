'''

# KMeans实现数据聚类 #

**** 任务 ****
基于task1_data1数据，建立Kmeans模型，实现数据聚类。

**** 主要任务流程 ****
1、K=2，实现数据聚类，可视化聚类结果、聚类中心；
2、已知第一个样本点X1=82.5,X2=67.9属于类别0，对聚类结果进行矫正；
3、基于task1_data2建立KNN模型，思考其与聚类结果的差异
4、修改Kmeans迭代次数与初始化参数，查看模型迭代过程中的结果变化

task1_data1：包含了无标签数据及一个带有标签的样本点；
task1_data2：包含了正确类别标签结果的数据，可用于模型评估与监督学习

'''

#数据加载
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('task1_data1.csv')
data_result = pd.read_csv('task1_data2.csv')
#X 赋值
X = data

#建立KMeans模型并训练
from sklearn.cluster import KMeans
KM = KMeans(n_clusters=2,init='random',random_state=0)  # n_clusters=2,
                                                        # init='random' 指一开始聚类中心随机设置
                                                        # random_state=0 表示可以一直重复寻找聚类中心直至收敛。若要设置迭代次数，则设置random_state=1,n_init=1,max_iter=5
KM.fit(X)

#查看聚类中心
centers = KM.cluster_centers_
print(centers)

#无监督聚类结果预测
y_predict = KM.predict(X)

#准确率计算
from sklearn.metrics import accuracy_score
y = data_result['y']
accuracy = accuracy_score(y,y_predict)
print(accuracy)

fig,axes = plt.subplots(1,2,figsize=(16,8))

axes[0].scatter(X.loc[:,'x1'][y_predict==0],X.loc[:,'x2'][y_predict==0],label='label0')
axes[0].scatter(X.loc[:,'x1'][y_predict==1],X.loc[:,'x2'][y_predict==1],label='label1')
axes[0].set_title('unlabeled data (predicted result)')
axes[0].set_xlabel('x1')
axes[0].set_ylabel('x2')

axes[1].scatter(X.loc[:,'x1'][y==0],X.loc[:,'x2'][y==0],label='label0')
axes[1].scatter(X.loc[:,'x1'][y==1],X.loc[:,'x2'][y==1],label='label1')
axes[1].set_title('labeled data')
axes[1].set_xlabel('x1')
axes[1].set_ylabel('x2')
plt.legend(loc='best')
plt.savefig('result.png')

#逐步迭代查看KMeans模型训练效果
centers = np.array([[0,0,0,0]])
for i in range(1,10):
    KM = KMeans(n_clusters=2,random_state=1,init='random',n_init=1,max_iter=i)
    KM.fit(X)

    centers_i = KM.cluster_centers_
    centers_i_temp = centers_i.reshape(1,-1)
    centers = np.concatenate((centers,centers_i_temp),axis=0)
    #predict based on training data
    y_predict = KM.predict(X)

    #visualize the data and results
    fig_i = plt.figure()
    label0 = plt.scatter(X.loc[:,'x1'][y_predict==0],X.loc[:,'x2'][y_predict==0])
    label1 = plt.scatter(X.loc[:,'x1'][y_predict==1],X.loc[:,'x2'][y_predict==1])

    plt.title("predicted data")
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.legend((label0,label1),('label0','label1'), loc='upper left')
    plt.scatter(centers_i[:,0],centers_i[:,1])
    fig_i.savefig('2d_output/{}.png'.format(i),dpi=500,bbox_inches = 'tight')

'''

KMeans实现数据聚类实战summary：

1、通过建立Kmeans模型，实现了无结果标签数据的自动归类（聚类），能有效地把数据根据实际类别划分成两类，但类别名称与实际相反；
2、通过观察并对比存在类别标签地样本，完成了结果矫正，矫正后的模型能很好的预测样本类别；
3、通过建立KNN模型，实现了对样本数据的有效分类，不需要经过额外的矫正步骤；
4、掌握了观察模型训练过程地方法，有助于加深对其的理解

核心算法参考链接：https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

'''