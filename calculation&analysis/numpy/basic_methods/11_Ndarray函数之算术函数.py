'''

                    ******** Numpy 算术函数 ********

numpy.add()         两个数组相加   !!! 数组必须具有相同的形状或符合数组广播规则。 !!!
numpy.subtract()    两个数组相减   !!! 数组必须具有相同的形状或符合数组广播规则。 !!!
numpy.multiply()    两个数组相乘   !!! 数组必须具有相同的形状或符合数组广播规则。 !!!
numpy.divide()      两个数组相除   !!! 数组必须具有相同的形状或符合数组广播规则。 !!!

numpy.reciprocal()  返回数组中每个元素的倒数。如 1/4 倒数为 4/1。
numpy.power()       将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂。
numpy.mod()         计算输入数组中相应元素的相除后的余数。
numpy.remainder()   与 numpy.mod() 效果相同。

'''
import numpy as np
# 相同的形状的数组加减乘除
a = np.arange(9, dtype = np.float_).reshape(3,3)
b = np.array([10,10,10])
print('两个数组相加：\n',np.add(a,b))
print('两个数组相减：\n',np.subtract(a,b))
print('两个数组相乘：\n',np.multiply(a,b))
print('两个数组相除：\n',np.divide(a,b))

# numpy.reciprocal()  返回数组中每个元素的倒数。
c = np.arange(1,10, dtype = np.float_).reshape(3,3)
print('原数组：\n',c,'\n倒数：\n',np.reciprocal(c))

# numpy.power()       将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂。
d = np.array([10,100,1000])
e = np.array([1,2,3])
print ('调用 power 函数，并使用一个整数作为全部元素的幂：\n',np.power(d,2))
print ('调用 power 函数，并使用一个数组作为相应元素的幂：\n',np.power(d,e))

# numpy.mod() / numpy.remainder()        计算输入数组中相应元素的相除后的余数。
f = np.array([10,20,30])
g = np.array([3,5,7])
print('调用 mod() / remainder() 函数：\n',np.mod(f,g),np.remainder(f,g))