'''

        ******** Numpy 数组操作函数主要包含了以下几类 ********
修改数组形状 | 翻转数组 | 修改数组维度 | 连接数组 | 分割数组 | 数组元素的添加与删除

        ******** Numpy 数组操作函数之连接数组 ********

numpy.concatenate((a1, a2, ...), axis) 函数用于沿指定轴连接相同形状的两个或多个数组
        a1, a2, ...：相同类型的数组
        axis：沿着它连接数组的轴，默认为 0

numpy.stack(arrays, axis) 函数用于沿新轴连接数组序列(生成高一维的数组）
        arrays相同形状的数组序列
        axis：返回数组中的轴，输入数组沿着它来堆叠

numpy.hstack 是 numpy.stack 函数的变体，它通过水平堆叠来生成数组。
numpy.vstack 是 numpy.stack 函数的变体，它通过垂直堆叠来生成数组。
'''
import numpy as np
# numpy.concatenate((a1, a2, ...), axis) 函数用于沿指定轴连接相同形状的两个或多个数组
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print('沿轴 0 连接两个数组：\n',np.concatenate((a, b)))
print('沿轴 1 连接两个数组：\n',np.concatenate((a, b), axis=1))

# numpy.stack(arrays, axis) 函数用于沿新轴连接数组序列(生成高一维的数组）
import numpy as np
print('沿轴 0 堆叠两个数组：\n',np.stack((a, b), 0))
print('沿轴 1 堆叠两个数组：\n',np.stack((a, b), 1))



