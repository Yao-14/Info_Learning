'''

                    ******** Numpy 舍入函数 ********

numpy.around(a,decimals) 函数返回指定数字的四舍五入值。
        decimals: 舍入的小数位数。 默认值为0。 如果为负，整数将四舍五入到小数点左侧的位置

numpy.floor(a) 返回小于或者等于指定表达式的最大整数，即向下取整。

numpy.ceil(a) 返回大于或者等于指定表达式的最小整数，即向上取整。


'''
import numpy as np

a = np.array([1.0,5.55,  123,  0.567,  25.532])
print (np.around(a))
print (np.around(a, decimals = 1))
print (np.around(a, decimals = -1))

b = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
print (np.floor(b))

c = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
print (np.ceil(c))