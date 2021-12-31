'''

        ******** Numpy 数组操作函数主要包含了以下几类 ********
修改数组形状 | 翻转数组 | 修改数组维度 | 连接数组 | 分割数组 | 数组元素的添加与删除

        ******** Numpy 数组操作函数之翻转数组 ********
numpy.transpose(arr, axes)  对换数组的维度
        arr：要操作的数组
        axes：整数列表，对应维度，通常所有维度都会对换。（e.g. np.transpose(a, axes=(1,2,0)))

numpy.ndarray.T 	和 numpy.transpose() 相同，对换数组的维度

numpy.rollaxis(arr, axis, start)    向后滚动特定的轴到一个特定位置
        arr：数组
        axis：要向后滚动的轴，其它轴的相对位置不会改变
        start：默认为零，表示完整的滚动。会滚动到特定位置。

numpy.swapaxes(arr, axis1, axis2)   用于交换数组的两个轴
        arr：输入的数组
        axis1：对应第一个轴的整数
        axis2：对应第二个轴的整数
'''
import numpy as np

a = np.arange(12).reshape(3, 4)
# numpy.transpose(arr, axes)  对换数组的维度
print(a,'\n',np.transpose(a))
# numpy.ndarray.T 	和 numpy.transpose() 相同，对换数组的维度
print(a,'\n',a.T)

b = np.arange(12).reshape(3, 2, 2)
# numpy.rollaxis(arr, axis, start)    向后滚动特定的轴到一个特定位置
print (b,'\n',np.rollaxis(b,2,0))   # 将轴 2 滚动到轴 1（宽度到高度）
# numpy.swapaxes(arr, axis1, axis2)   用于交换数组的两个轴
print (b,'\n',np.swapaxes(b, 0, 1))
