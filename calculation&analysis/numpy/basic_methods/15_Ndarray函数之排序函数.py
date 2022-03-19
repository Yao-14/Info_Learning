'''

NumPy 提供了多种排序排序算法。 下表显示了三种排序算法的比较：

        种类	           速度	      最坏情况	 工作空间	      稳定性
'quicksort'（快速排序）	1	    O(n^2)	        0	        否
'mergesort'（归并排序）	2	    O(n*log(n))	    ~n/2	    是
'heapsort'（堆排序）	    3	    O(n*log(n))	    0	        否

                    ******** Numpy 排序函数 ********

numpy.sort(a, axis, kind, order) 函数返回输入数组的排序副本。
        a: 要排序的数组
        axis: 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序， axis=0 按列排序，axis=1 按行排序
        kind: 默认为'quicksort'（快速排序）
        order: 如果数组包含字段，则是要排序的字段

numpy.argsort(a)     函数返回的是数组值从小到大的索引值。
numpy.lexsort(a,b,c) 用于对多个序列进行排序。把它想象成对电子表格进行排序，每一列代表一个序列，排序时优先照顾靠后的列。
numpy.msort(a)	     数组按第一个轴排序，返回排序后的数组副本。np.msort(a) 相等于 np.sort(a, axis=0)。
numpy.sort_complex(a)	对复数按照先实部后虚部的顺序进行排序。
numpy.partition(a, kth[, axis, kind, order])	指定一个数，对数组进行分区
numpy.argpartition(a, kth[, axis, kind, order])	可以通过关键字 kind 指定算法沿着指定轴对数组进行分区

'''
import numpy as np
# numpy.sort(a, axis, kind, order) 函数返回输入数组的排序副本。
a = np.array([[3, 7], [9, 1]])
print('我们的数组是：\n',a)
print('调用 sort() 函数，不含axis：\n',np.sort(a,axis=None))
print('按列排序：\n',np.sort(a, axis=0))
print('按行排序：\n',np.sort(a, axis=1))
# 在 sort 函数中排序字段
dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)
print('我们的数组是：\n',a)
print('按 name 排序：\n',np.sort(a, order='name'))

# numpy.argsort(a)          函数返回的是数组值从小到大的索引值。
x = np.array([3, 1, 2])
y = np.argsort(x)
print('原数组是：\n',x)
print('对 x 调用 argsort() 函数：\n',y)
print('以排序后的顺序重构原数组：\n',x[y])

# numpy.lexsort(a,b,c)      用于对多个序列进行排序。把它想象成对电子表格进行排序，每一列代表一个序列，排序时优先照顾靠后的列。
nm =  ('raju','anil','ravi','amar')
dv =  ('f.y.',  's.y.',  's.y.',  'f.y.')
ind = np.lexsort((dv,nm))
print ('调用 lexsort() 函数：\n',ind)
print ('使用这个索引来获取排序后的数据：\n',[nm[i]  +  ", "  + dv[i]  for i in ind])

# numpy.sort_complex(a)	    对复数按照先实部后虚部的顺序进行排序。
print(np.sort_complex([5, 3, 6, 2, 1]))
print(np.sort_complex([1 + 2j, 2 - 1j, 3 - 2j, 3 - 3j, 3 + 5j]))

# numpy.partition(a, kth[, axis, kind, order])	    指定一个数，对数组进行分区
a = np.array([3, 4, 2, 1])
print(np.partition(a, 3))       # 将数组 a 中所有元素（包括重复元素）从小到大排列，3 表示的是排序数组索引为 3 的数字，比该数字小的排在该数字前面，比该数字大的排在该数字的后面
print(np.partition(a, (1, 3)))  # 小于 1 的在前面，大于 3 的在后面，1和3之间的在中间
