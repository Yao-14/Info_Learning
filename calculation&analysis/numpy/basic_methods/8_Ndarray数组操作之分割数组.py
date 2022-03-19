'''

        ******** Numpy 数组操作函数主要包含了以下几类 ********
修改数组形状 | 翻转数组 | 修改数组维度 | 连接数组 | 分割数组 | 数组元素的添加与删除

        ******** Numpy 数组操作函数之分割数组 ********

numpy.split(ary, indices_or_sections, axis) 函数沿特定的轴将数组分割为子数组
        ary：被分割的数组
        indices_or_sections：果是一个整数，就用该数平均切分，如果是一个数组，为沿轴切分的位置（左开右闭）
        axis：设置沿着哪个方向进行切分，默认为 0，横向切分，即水平方向。为 1 时，纵向切分，即竖直方向。

numpy.hsplit 函数用于水平分割数组，通过指定要返回的相同形状的数组数量来拆分原数组。
numpy.vsplit 函数用于垂直分割数组，通过指定要返回的相同形状的数组数量来拆分原数组。


'''
import numpy as np

a = np.arange(9)
print('将数组分为三个大小相等的子数组：\n',np.split(a, 3))
print('将数组在一维数组中表明的位置分割：\n',np.split(a, [4, 7]))
b = np.arange(16).reshape(4, 4)
print('默认分割（0轴，即水平方向分割）：\n',np.split(b,2))
print('沿垂直方向分割：\n',np.split(b,2,axis = 1))
