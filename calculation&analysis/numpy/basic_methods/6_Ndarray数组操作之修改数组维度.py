'''

        ******** Numpy 数组操作函数主要包含了以下几类 ********
修改数组形状 | 翻转数组 | 修改数组维度 | 连接数组 | 分割数组 | 数组元素的添加与删除

        ******** Numpy 数组操作函数之修改数组维度 ********

numpy.expand_dims(arr, axis) 函数通过在指定位置插入新的轴来扩展数组形状
        arr：输入数组
        axis：新轴插入的位置

numpy.squeeze(arr, axis) 函数从给定数组的形状中删除一维的条目
        arr：输入数组
        axis：整数或整数元组，用于选择形状中一维条目的子集

'''
import numpy as np

# numpy.expand_dims(arr, axis) 函数通过在指定位置插入新的轴来扩展数组形状
x = np.array(([1, 2], [3, 4]))
y = np.expand_dims(x, axis=0)
print('数组 y：\n',y)
print('数组 x 和 y 的形状：',x.shape, y.shape)

y = np.expand_dims(x, axis=1)
print('在位置 1 插入轴之后的数组 y：\n',y)
print('x.ndim 和 y.ndim：',x.ndim, y.ndim)
print('x.shape 和 y.shape：',x.shape, y.shape)


# numpy.squeeze(arr, axis) 函数从给定数组的形状中删除一维的条目
x = np.arange(9).reshape(3, 3,1)
print('数组 x：\n',x)
y = np.squeeze(x)
print('数组 y：\n',y)
print('数组 x 和 y 的形状：\n',x.shape, y.shape)
