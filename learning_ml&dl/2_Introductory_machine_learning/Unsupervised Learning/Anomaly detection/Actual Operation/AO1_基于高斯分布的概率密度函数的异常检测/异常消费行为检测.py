'''

# 异常消费行为检测 #

**** 任务 ****
基于task1_data数据，基于高斯分布的概率密度函数实现异常消费行为检测。

**** 主要任务流程 ****
1、可视化消费数据、数据分布次数、及其对应高斯分布的概率密度函数；
2、设置异常样本比例0.03，建立模型，实现异常数据点预测
3、可视化异常检测处理结果
4、修改异常样本比例为0.1、0.2，查看比例改变对结果的影响
5、能力拓展：修改异常样本比例为0-0.2，以0.01为递增间隔，查看保存结果、生成动态gif图

'''

#数据加载
import pandas as pd
import numpy as np
data = pd.read_csv('task1_data.csv')
data.head()

#数据可视化
from matplotlib import pyplot as plt
fig1 = plt.figure()
plt.scatter(data.loc[:,'frequency'],data.loc[:,'payment'],marker='x')
plt.title('raw data')
plt.xlabel('frequency')
plt.ylabel('payment')
plt.show()

#x1 x2 X赋值
X = data
x1 = data.loc[:,'frequency']
x2 = data.loc[:,'payment']

#数据分布的可视化操作
fig2 = plt.figure(figsize=(20,5))
fig2_1 = plt.subplot(121)
plt.hist(x1,bins=100)
plt.title('frequency data')
plt.xlabel('frequency')
plt.ylabel('counts')

fig2_2 = plt.subplot(122)
plt.hist(x2,bins=100)
plt.title('payment data')
plt.xlabel('payment')
plt.ylabel('counts')
plt.show()

#计算平均值u，以及标准差sigma
x1_mean = x1.mean()
x1_sigma = x1.std()
x2_mean = x2.mean()
x2_sigma = x2.std()
print(x1_mean,x1_sigma,x2_mean,x2_sigma)

#计算基于高斯分布的概率密度函数
from scipy.stats import norm    #norm 对应正态分布
x1_range = np.linspace(0,10,300)
x1_normal = norm.pdf(x1_range,x1_mean,x1_sigma)     # norm.pdf生成对应曲线
x2_range = np.linspace(0,400,300)
x2_normal = norm.pdf(x2_range,x2_mean,x2_sigma)
# print(x1_range,x1_range.shape)
print(x1_normal,x1_normal.shape)

#原始数据的高斯分布概率密度函数可视化
fig3 = plt.figure(figsize=(20,5))
fig3_1 = plt.subplot(121)
plt.plot(x1_range,x1_normal)
plt.title('x1(frequency) Gaussian Distribution')
plt.xlabel('x1(frequency)')
plt.ylabel('p(x1)')

fig3_2 = plt.subplot(122)
plt.plot(x2_range,x2_normal)
plt.title('x2(payment) Gaussian Distribution')
plt.xlabel('x2(payment)')
plt.ylabel('p(x2)')
plt.show()

import math
#设置范围
x_min, x_max = 0, 10
y_min, y_max = 0, 400
h1 = 0.1
h2 = 0.1
#生成矩阵数据
xx, yy = np.meshgrid(np.arange(x_min, x_max, h1), np.arange(y_min, y_max, h2))
print(xx.shape,yy.shape)

#展开矩阵数据
x_range = np.c_[xx.ravel(), yy.ravel()]
x1 = np.c_[xx.ravel()]
x2 = np.c_[yy.ravel()]
x_range_df = pd.DataFrame(x_range)
#x_range_df.to_csv('data.csv')
#高斯分布参数
u1 = x1_mean
u2 = x2_mean
sigma1 = x1_sigma
sigma2 = x2_sigma
#计算高斯分布概率
p1 = 1/sigma1/math.sqrt(2*math.pi)*np.exp(-np.power((x1-u1),2)/2/math.pow(sigma1,2))
p2 = 1/sigma2/math.sqrt(2*math.pi)*np.exp(-np.power((x2-u2),2)/2/math.pow(sigma2,2))
p = np.multiply(p1,p2)
#对概率密度维度转化
p_2d = p.reshape(xx.shape[0],xx.shape[1])

#综合高斯分布概率密度函数的可视化
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
fig5 = plt.figure()
axes3d = Axes3D(fig5)
axes3d.plot_surface(xx,yy,p_2d,cmap=cm.rainbow)

#建立异常检测模型
from sklearn.covariance import EllipticEnvelope
model = EllipticEnvelope(contamination=0.03)    #contamination 设置概率密度阈值
model.fit(X)
print(X)
#模型预测
y_predict = model.predict(X)
print(y_predict)
fig6 = plt.figure()
plt.scatter(data.loc[:,'frequency'],data.loc[:,'payment'],marker='x',label='raw data')
plt.scatter(data.loc[:,'frequency'][y_predict==-1],data.loc[:,'payment'][y_predict==-1],marker='o',facecolor='none',edgecolor='red',s=150,label='anomaly_data')

plt.title('raw data')
plt.xlabel('frequency')
plt.ylabel('payment')
plt.legend()
plt.show()

'''

异常消费行为检测实战summary：

1、实现了消费数据、数据分布次数、及其对应高斯分布的概率密度函数的可视化；
2、建立了异常数据检测模型，根据预先设定的异常数据比例，自动寻找到了数据中的异常点；
3、实现了预测结果可视化，有助于评估模型表现及快速验证模型效果；
4、通过修改异常数据比例参数contamination，帮助我们更好的理解算法的原理;

核心算法参考链接：https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html


'''