import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(-1, 1, 4)
y = np.random.uniform(-1, 1, 4)
p1, = plt.plot([1, 2, 3])
p2, = plt.plot([3, 2, 1])
p3 = plt.scatter(x[0:2], y[0:2], marker='D', color='r')
p4 = plt.scatter(x[2:], y[2:], marker='D', color='g')
p5 = plt.scatter(x[0:2], y[2:4], marker='D', color='r')
p6 = plt.scatter(x[2:], y[2:], marker='D', color='g')
#如何在一张图中设置多个图例,每个图例所含的内容数量必须大于等于2
#设置图例1
l1 = plt.legend([p1, p2], ["line 1", "line 2"], loc='upper left')
plt.gca().add_artist(l1)
#设置图例2
l2 = plt.legend([p3, p4], ['label 3', 'label 4'], loc='lower right', scatterpoints=1)
plt.gca().add_artist(l2)
#设置图例3
plt.legend([p4,p5, p6], ['label 4','label 5', 'label 6'], loc='upper right')

plt.show()