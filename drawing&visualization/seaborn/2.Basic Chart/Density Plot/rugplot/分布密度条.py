'''
seaborn.rugplot():密度分布观测条绘制,通过观测条的粗细和疏密表示密度大小。一般同kdeplot或distplot一同绘制。
'''
import seaborn as sns
import matplotlib.pyplot as plt
list1 = [1, 1, 1, 1, 2, 3, 2, 2, 2, 1, 3, 4, 5, 7, 1, 1, 3, 4, 6, 2]
list2 = [3,2,4,8,6,1,3,5,1,0,6,2,9,6,4,1,2,7,3,2]
#绘制x轴上的观测条
sns.rugplot(x=list1,height=0.05 ,color = 'g', alpha = 0.5,label = '1')
#绘制x轴上的观测条
sns.rugplot(y=list2,height=0.05 ,color = 'r', alpha = 0.5,label = '2')
plt.legend()
plt.show()