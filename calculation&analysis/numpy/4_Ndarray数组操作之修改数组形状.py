'''

        ******** Numpy 数组操作函数主要包含了以下几类 ********
修改数组形状 | 翻转数组 | 修改数组维度 | 连接数组 | 分割数组 | 数组元素的添加与删除

        ******** Numpy 数组操作函数之修改数组形状 ********
numpy.ndarray.reshape( newshape, order='C')     可以在不改变数据的条件下修改形状.
        newshape：整数或者整数数组，新的形状应当兼容原有形状
        order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'k' -- 元素在内存中的出现顺序
numpy.ndarray.ravel(order='C')     展平的数组元素，返回一份数组拷贝（数组转化为 1 维），对拷贝所做的修改会影响原始数组。
        order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序
numpy.ndarray.flatten(order='C')   展平的数组元素，返回一份数组拷贝（数组转化为 1 维），对拷贝所做的修改不会影响原始数组。
        order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序
numpy.ndarray.flat     是一个数组元素迭代器，将数组中的所有数据依次输出（不管数组形状如何）。
'''
import numpy as np
a = np.arange(8)

# numpy.ndarray.reshape(newshape, order='C')   可以在不改变数据的条件下修改形状.
b = a.reshape(2,4)
print(a,'\n',b)

# numpy.ndarray.flat()  是一个数组元素迭代器，将数组中的所有数据依次输出（不管数组形状如何）。
for element in b.flat:
    print (element)

# numpy.ndarray.flatten(order='C')   返回一份数组拷贝（同时将数组转化为 1 维），对拷贝所做的修改不会影响原始数组。
print (b.flatten(order='C'),b.flatten(order='F'),b.flatten(order='A'),b.flatten(order='K'))

# numpy.ndarray.ravel(order='C')   展平的数组元素，顺序通常是"C风格"，返回的是数组视图（view），修改会影响原始数组。
print (b.ravel(order = 'C'),b.ravel(order = 'F'),b.ravel(order = 'A'),b.ravel(order = 'K'))
