import numpy as np

'''
NumPy 数组的维数称为秩（rank），秩就是轴的数量，即数组的维度，一维数组的秩为 1，二维数组的秩为 2，以此类推。

在 NumPy中，每一个线性的数组称为是一个轴（axis），也就是维度（dimensions）。比如说，二维数组相当于是两个一维数组，其中第一个一维数组中每个元素又是一个一维数组。所以一维数组就是 NumPy 中的轴（axis），第一个轴相当于是底层数组，第二个轴是底层数组里的数组。而轴的数量——秩，就是数组的维数。

很多时候可以声明 axis。axis=0，表示沿着第 0 轴进行操作，即对每一列进行操作；axis=1，表示沿着第1轴进行操作，即对每一行进行操作。

NumPy 的数组中比较重要 ndarray 对象属性有：
    ndarray.ndim	    秩，即轴的数量或维度的数量
    ndarray.shape	    数组的维度，对于矩阵，n 行 m 列
    ndarray.size	    数组元素的总个数，相当于 .shape 中 n*m 的值
    ndarray.dtype	    ndarray 对象的元素类型
    ndarray.itemsize	ndarray 对象中每个元素的大小，以字节为单位
    ndarray.real	    ndarray元素的实部
    ndarray.imag	    ndarray 元素的虚部
    ndarray.data	    包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。
    ndarray.flags	    ndarray 对象的内存信息，包含以下属性：
                                            C_CONTIGUOUS (C)	数据是在一个单一的C风格的连续段中
                                            F_CONTIGUOUS (F)	数据是在一个单一的Fortran风格的连续段中
                                            OWNDATA (O)	        数组拥有它所使用的内存或从另一个对象中借用它
                                            WRITEABLE (W)	    数据区域可以被写入，将该值设置为 False，则数据为只读
                                            ALIGNED (A)	        数据和所有元素都适当地对齐到硬件上
                                            UPDATEIFCOPY (U)	这个数组是其它数组的一个副本，当这个数组被释放时，原数组的内容将被更新
'''
list1 = [[[1,2,3,4,5],[3,5,2,7,1],[7,1,5,2,1]]]
array1 = np.array(list1)
#查看ndarray属性的指令
print(array1.size)  # size函数查看数组元素的总个数
print(array1.shape) # shape函数查看数组的维度
print(array1.ndim)  # ndim函数查看数组的维数
print(array1.dtype) # atype函数查看数组的元素类型