'''

        ******** Numpy 数组操作函数主要包含了以下几类 ********
修改数组形状 | 翻转数组 | 修改数组维度 | 连接数组 | 分割数组 | 数组元素的添加与删除

        ******** Numpy 数组操作函数之数组元素的添加与删除 ********

numpy.resize(arr, shape) 函数返回指定大小的新数组。如果新数组大小大于原始大小，则包含原始数组中的元素的副本。
        arr：要修改大小的数组
        shape：返回数组的新形状

numpy.append(arr, values, axis=None) 函数在数组的末尾添加值。 追加操作会分配整个数组，并把原来的数组复制到新数组中。 此外，输入数组的维度必须匹配否则将生成ValueError。
        arr：输入数组
        values：要向arr添加的值，需要和arr形状相同（除了要添加的轴）
        axis：默认为 None。当axis无定义时，是横向加成，返回总是为一维数组！当axis有定义的时候，分别为0和1的时候。当axis有定义的时候，分别为0和1的时候（列数要相同）。当axis为1时，数组是加在右边（行数要相同）。

numpy.insert(arr, obj, values, axis) 函数在给定索引之前，沿给定轴在输入数组中插入值。
                                     如果值的类型转换为要插入，则它与输入数组不同。 插入没有原地的，函数会返回一个新数组。 此外，如果未提供轴，则输入数组会被展开。
        arr：输入数组
        obj：在其之前插入值的索引
        values：要插入的值
        axis：沿着它插入的轴，如果未提供，则输入数组会被展开

numpy.delete(arr, obj, axis) 函数返回从输入数组中删除指定子数组的新数组。 与 insert() 函数的情况一样，如果未提供轴参数，则输入数组将展开。
        arr：输入数组
        obj：可以被切片，整数或者整数数组，表明要从输入数组删除的子数组
        axis：沿着它删除给定子数组的轴，如果未提供，则输入数组会被展开

numpy.unique(arr, return_index, return_inverse, return_counts) 函数用于去除数组中的重复元素。
        arr：输入数组，如果不是一维数组则会展开
        return_index：如果为true，返回新列表元素在旧列表中的位置（下标），并以列表形式储
        return_inverse：如果为true，返回旧列表元素在新列表中的位置（下标），并以列表形式储
        return_counts：如果为true，返回去重数组中的元素在原数组中的出现次数

'''
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
# numpy.resize(arr, shape) 函数返回指定大小的新数组。如果新数组大小大于原始大小，则包含原始数组中的元素的副本。
print(a,'\n',np.resize(a, (3, 1)),'\n',np.resize(a, (3, 3)))

# numpy.append(arr, values, axis=None) 函数在数组的末尾添加值。
print('未传递 Axis 参数。 在插入之前输入数组会被展开为一维数组：\n',np.append(a, [7, 8, 9]))  #若axis=None, append 函数返回的始终是一个一维数组。
print('沿轴 0 添加元素：\n',np.append(a, [[7, 8, 9]], axis=0))                         #若axis=0/1, append 函数返回的是修改后的数组形式。
print('沿轴 1 添加元素：\n',np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1))

# numpy.insert(arr, obj, values, axis) 函数在给定索引之前，沿给定轴在输入数组中插入值。
print('未传递 Axis 参数。 在插入之前输入数组会被展开为一维数组：\n',np.insert(a, 3, [11, 12]))
print('沿轴 0 广播：\n',np.insert(a, 1, [11], axis=0))
print('沿轴 1 广播：\n',np.insert(a, 1, 11, axis=1))

# numpy.delete(arr, obj, axis) 函数返回从输入数组中删除指定子数组的新数组。
print('未传递 Axis 参数。 在插入之前输入数组会被展开：\n',np.delete(a, 5))
print('删除第二列：\n',np.delete(a, 1, axis=1))
print('包含从数组中删除的替代值的切片：\n',np.delete(a, np.s_[::2]))

# numpy.unique(arr, return_index, return_inverse, return_counts) 函数用于去除数组中的重复元素。
a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
print('去重后的数组：\n',np.unique(a))

b, indices = np.unique(a, return_index=True)
print('返回新列表元素在旧列表中的位置（下标）：\n',indices)

c, indices = np.unique(a, return_inverse=True)
print('返回旧列表元素在新列表中的位置（下标）：\n',indices)
print('使用下标重构原数组：\n',c[indices])

print('返回去重元素的重复数量：')
u, indices = np.unique(a, return_counts=True)
print(u)
print(indices)
