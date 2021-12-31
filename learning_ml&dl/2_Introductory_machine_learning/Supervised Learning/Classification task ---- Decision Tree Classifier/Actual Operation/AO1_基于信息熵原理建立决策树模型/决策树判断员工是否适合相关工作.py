'''

# 决策树判断员工是否适合相关工作实战task #

**** 任务 ****
基于课程中决策树案例与task1_data数据，基于信息熵原理建立决策树模型判断员工是否适合相关工作。

**** 主要任务流程 ****
1、建立决策树模型、计算准确率
2、预测申请者skill=1,experice=0,degree=1,Income=1是否适合该工作；
3、可视化模型结构
4、修改min_samples_leaf参数，对比模型结果
能力拓展：基于ID3原理计算每个节点信息熵增益，画出决策树结构，与实战模型结构对比

**** 决策树主要流程 ****
1、数据加载并可视化
2、数据预处理
3、建立逻辑回归模型，训练模型
4、模型预测结果
5、评估模型表现及可视化模型结构

'''
#数据加载（此处数据以转换，将所有数据转换为数值形式）
import pandas as pd
import numpy as np
data = pd.read_csv('data.csv')

#数据预处理
X = data.drop(['y'],axis=1)
y = data.loc[:,'y']

#建立决策树模型
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='entropy',min_samples_leaf=50)  # criterion='entropy' 指以信息熵的变化作为建立树结构的标准
                                                                         # min_samples_leaf 指建立树结构最小分支的样本数
#模型训练
model.fit(X,y)

#模型预测
y_predict = model.predict(X)

#模型评估（准确率指标评估）
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y,y_predict)
print(accuracy)

#测试样本预测
X_test = np.array([[1,0,1,1]])
y_test_predict = model.predict(X_test)
print('适合' if y_test_predict==1 else '不适合')

#可视化模型结构
from matplotlib import pyplot as plt
from sklearn import tree
tree.plot_tree(model,filled='True',feature_names=['Skill','Experience','Degree','Income'],class_names=['Un-qualified','Qualified'])
plt.savefig('result.png')

'''

决策树判断员工是否适合相关工作实战summary：
1、通过建立决策树模型，实现了基于不同属性的分级判断，达到了预测申请者是否适合对应岗位的目标，模型准确率0.85；
2、对新申请者skill=1,experice=0,degree=1,Income=1进行预测，判断其适合该岗位
3、实现了决策树模型结果可视化，并完成存储
4、通过修改叶子节点最少样本数对应参数min_samples_leaf，简化了模型结构，判断逻辑更加清晰，模型准确率轻微下降至0.83；

核心算法参考链接：https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

'''