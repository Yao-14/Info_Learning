'''

                    ******** Numpy 条件筛选函数 ********

numpy.argmax()  函数沿给定轴返回最大元素的索引。(展开为一维数组）

numpy.argmin()  函数沿给定轴返回最小元素的索引。(展开为一维数组）

numpy.nonzero() 函数返回输入数组中非零元素的索引。(展开为一维数组）

numpy.where()   函数返回输入数组中满足给定条件的元素的索引。(展开为一维数组）

'''

import numpy as np
# numpy.argmax()  函数沿给定轴返回最大元素的索引。(展开为一维数组）
# numpy.argmin()  函数沿给定轴返回最小元素的索引。(展开为一维数组）
a1 = np.array([[30,40,70],[80,20,10],[50,90,60]])
i1 = np.argmax(a1,axis=1)
i2 = np.argmax(a1)
print ('最大元素的索引：\n',i1)
print ('最大元素的索引：\n',i2)

# numpy.nonzero() 函数返回输入数组中非零元素的索引。(展开为一维数组）
a3 = np.array([[30,40,0],[0,20,10],[50,0,60]])
i3 = np.nonzero (a3)
print ('非零元素的索引：\n',i3)
print('使用这些索引来获取满足条件的元素：\n',a3[i3])
1
# numpy.where()   函数返回输入数组中满足给定条件的元素的索引。(展开为一维数组）
a4 = np.arange(9.).reshape(3, 3)
i4 = np.where(a4 > 3)
print('大于 3 的元素的索引：\n',i4)
print('使用这些索引来获取满足条件的元素：\n',a4[i4])