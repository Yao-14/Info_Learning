import numpy as np

list1 = [[[1,2,3,4,5],[3,5,2,7,1],[7,1,5,2,1]]]
''' 手动创建ndarray '''
# numpy.array(object, dtype = None, ndmin = 0，order = None) 创建一个 ndarray
print(np.array(list1, dtype = None, order = None, ndmin=0))      # （dtype：指定数组元素的数据类型，可选；ndmin：指定生成数组的最小维度；order：创建数组的样式，C为行方向，F为列方向，A为任意方向（默认））
# numpy.asarray 类似 numpy.array，但可以输入任意形式的参数，可以是列表、列表的元组、元组、元组的元组、元组的列表、多维数组等。
print(np.asarray(list1, dtype = None, order = None))

''' 函数创建ndarray方法1 '''
# np.zeros(shape, dtype) 创建指定大小的数组，数组元素以 0 来填充
print(np.zeros((5,5)))
# np.ones(shape, dtype)  创建指定形状的数组，数组元素以 1 来填充
print(np.ones((5,5)))

'''n函数创建ndarray方法2————从数值范围创建一维数组'''
# np.arange(start, stop, step, dtype) 根据 start 与 stop 指定的范围以及 step 设定的步长，生成一个 ndarray
print(np.arange(0,11,2))
# np.linspace(start, stop, num, endpoint, retstep,dtype) 在start和stop之间返回均匀间隔的num个数据,创建一个等差数列构
print(np.linspace(2,10,5)) # （endpoint：True则包含stop；False则不包含stop；retstep：即如果为True则结果会给出数据间隔)
# np.logspace(start, stop, num, endpoint, base, dtype)  在start和stop之间返回均匀间隔的num个数据,创建一个于等比数列
print(np.logspace(2,10,5)) # （endpoint：True则包含stop；False则不包含stop；retstep：即如果为True则结果会给出数据间隔；base：对数 log 的底数)
