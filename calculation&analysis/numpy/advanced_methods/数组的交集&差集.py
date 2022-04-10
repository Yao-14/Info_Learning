import numpy as np
a1 = np.asarray([[1,2,3],[3,4,5],[4,5,6]], order='C')
a2 = np.asarray([[3,4,2], [1,2,3], [3,4,5], [7,1,5]], order='C')
"""
由于numpy的ndarry形式可能是Fortran-style 也可能是C-style，这两种数组的行与列的表述方式是相反的，
而np.view（）是内存布局在数组上创建视图，导致输出dtype大小与内存中覆盖源数组的全长所需的字节数不完全匹配
解决办法:创建数组时a1 = np.asarray(a1, order='C')
"""
a1_rows = a1.view([('', a1.dtype)] * a1.shape[1])
a2_rows = a2.view([('', a2.dtype)] * a2.shape[1])
"""print(a1_rows)
print(a2_rows)"""

# 求两个数组的交集
inter_array = np.intersect1d(a1_rows, a2_rows).view(a1.dtype).reshape(-1, a1.shape[1])

# 获得交集数组的索引
inter_array2, inter_index1, inter_index2 = np.intersect1d(a1_rows, a2_rows, return_indices=True)
print(inter_index1)
print(inter_index2)
print(inter_array)

# 求两个数组的差集
diff_array = np.setdiff1d(a1_rows, a2_rows).view(a1.dtype).reshape(-1, a1.shape[1])
print(diff_array)

