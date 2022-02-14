"""
Dask Array 使用阻塞算法实现 NumPy ndarray 接口的一个子集，将大数组切割成许多小数组。这让我们可以使用我们所有的内核在大于内存的数组上进行计算。简单地说：Dask Array即分布式 Numpy，具有以下三大特点：

    并行：在计算机上使用所有的核心
    大于内存：通过将数组分解成许多小块，在这些小块上运行，使计算的内存占用最小，并有效地从磁盘中流出数据，从而在大于可用内存的数据集上工作。
    分块算法：通过执行许多较小的计算来完成较大的计算

Dask Array支持的NumPy 接口主要包括：

    1.Arithmetic and scalar mathematics: +, *, exp, log, ...
    2.Reductions along axes: sum(), mean(), std(), sum(axis=0), ...
    3.Tensor contractions / dot products / matrix multiply: tensordot
    4.Axis reordering / transpose: transpose
    5.Slicing: x[:100, 500:100:-2]
    6.Fancy indexing along single axes with lists or NumPy arrays: x[:, [10, 1, 5]]
    7.Array protocols like __array__ and __array_ufunc__
    8.Some linear algebra: svd, qr, solve, solve_triangular, lstsq


Dask Array 存在以下缺陷：

    1.很多np.linalg都没有实施。这是由许多优秀的 BLAS/LAPACK 实现完成的，并且是许多正在进行的学术研究项目的重点
    2.形状未知的数组不支持所有操作
    3.众所周知，像sort这样的操作很难并行执行，并且在非常大的数据上价值有所降低（您实际上很少需要完整的排序）。我们通常包括并行友好的替代方案，例如topk
    4.Dask Array 没有实现这样的操作tolist，对于较大的数据集来说效率非常低。同样，使用 for 循环遍历 Dask 数组的效率非常低
    5.Dask 开发是由即时需求驱动的，因此许多较少使用的功能尚未实现。鼓励社区贡献

Dask Array使用规范：

    1. 确定一个良好的 chunks，chunks大小和形状严重影响DASK的性能（chunks大小太小会导致性能大量开销，chunks形状与数据对齐不佳会导致读取效率低下）。
       同时chunks大小和形状需要保证可以多个chunk同时放入内存中（即每个chunk尽量小）。Dask 在内存中的chunk的数量通常是活动线程数的两倍。
       若是自己无法判断chunks的大小形状，则可以选择 chunks='auto' ， Dask Array 将查找一个 chunks属性并使用它来提供良好的分块。
    2. 考虑使用 Xarray，在处理复杂数据集时也增加了便利性，并且解决一部分Dask Array的问题：
        (1) 将多个数组作为一致的数据集一起管理
        (2) 一次从一堆 HDF 或 NetCDF 文件中读取
        (3) 使用一致的 API 在 Dask Array 和 NumPy 之间切换
    3. 在 Dask Array 中没有确切功能的计算时，我们可以使用一些更通用的函数来构建我们自己的函数，如 blockwise() map_blocks() map_overlap() reduction()。

"""

import time

# 比较使用NumPy和DASK计算分别耗时
## NumPy
import numpy as np
start_time = time.time()
x = np.random.normal(10, 0.1, size=(20000, 20000))
y = x.mean(axis=0)[::100]
print(f"CPU times via NumPy：{time.time() - start_time}")

## DASK
import dask.array as da
start_time = time.time()
da_x = da.random.normal(10, 0.1, size=(20000, 20000), chunks=(1000, 1000))
da_y = x.mean(axis=0)[::100]
da_y.compute()
print(f"CPU times via DASK：{time.time() - start_time}")



