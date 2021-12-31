'''

                            ******** Numpy Matrix ********
    Matrix矩阵：矩阵是一个由行（row）列（column）元素排列成的矩形阵列。矩阵里的元素可以是数字、符号或数学式。
    转置矩阵： numpy.transpose 或使用 T 属性，将 m 行 n 列的矩阵，转换为 n 行 m 列的矩阵。
                            ******** Numpy Matrix矩阵库创建矩阵函数 ********

numpy.empty()       创建一个新矩阵，数据是随机填充的。
numpy.zeros()       创建一个以 0 填充的矩阵。
numpy.ones()        创建一个以 1 填充的矩阵。
numpy.eye()         创建一个矩阵，对角线元素为 1，其他位置为零。
numpy.identity()    创建给定大小的单位矩阵。单位矩阵是个方阵，从左上角到右下角的对角线（称为主对角线）上的元素均为 1，除此以外全都为 0。

'''
import numpy as np
#numpy.empty()      创建一个新矩阵，数据是随机填充的。
print (np.empty((2,2)))
#numpy.zeros()      创建一个以 0 填充的矩阵。
print (np.zeros((2,2)))
#numpy.ones()       创建一个以 1 填充的矩阵。
print (np.ones((2,2)))
#numpy.eye()        创建一个矩阵，对角线元素为 1，其他位置为零。
print (np.eye(3, 4, dtype = float))
#numpy.identity()   创建给定大小的单位矩阵。
print (np.identity(5, dtype =float))

