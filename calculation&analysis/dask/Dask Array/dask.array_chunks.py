"""
chunks：将一个Array分割成 XxY 大小的 N 个块(chunk)，分别放入内存中进行运算。通过指定一个chunks参数来告诉 dask.array 如何将底层数组分解成块.

指定chunks的方式包括：

    1.一个统一的维度大小如1000，表示每个维度中大小1000的块
    2.一个统一的语块形状如(1000,2000,3000)，意思是第一轴1000个，第二轴2000个，第三轴3000个
    3.所有块沿所有维度的完全显式尺寸，如((1000,1000,500), (400,400), (5,5,5,5,5))
    4.一个字典，指定每个维度的块大小，如{0：1000，1：2000，2：3000}。这只是上面表格2和3的另一种写法

注意：chunks参数代表“块形状”而不是“块数量”，因此指定chunks=1意味着您将拥有许多块，每个块只有一个元素。
注意：chunks还包括三个特殊值：
        1.`-1` ———— no chunking along this dimension
        2.`None` ———— no change to the chunking along this dimension (useful for rechunk)
        3.`'auto'` ———— allow the chunking in this dimension to accommodate ideal chunk sizes
                        ("auto" 以尝试达到字节数等于配置值(array.chunk-size)的块大小， array.chunk-size默认情况下设置为 128MiB，但您可以在配置中更改。)

选择chunks需要考虑的因素：

    1.一个词块应该足够小，以便在内存中舒适地贴合。我们将同时拥有许多内存块
    2.块必须足够大，以至于该块上的计算量要远远长于Dask调度所导致的每个任务的1ms开销。一个任务需要100ms以上的时间
    3.根据RAM的可用性和计算时间的长短，10MB - 1GB之间的块大小比较常见
    4.语块应与所要做的计算一致。
      例如，如果您计划经常沿着特定的维度进行切片，那么如果您的块是对齐的，这样就更有效了，以至于您不得不接触较少的块。如果您想添加两个数组，那么如果这些数组具有匹配的块模式，则很方便
    5.语块应与您的存储对齐，如适用。
      阵列数据格式也经常被分块。在加载或保存数据时，如果有与存储块对齐的Dask数组块是有用的，则在每个方向上往往要大几倍

"""

import dask.array as da
import numpy as np

x = np.arange(0, 36, 1).reshape(6, 6)
"""
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]
 [24 25 26 27 28 29]
 [30 31 32 33 34 35]]
"""

"""展示不同的chunks值分割相同数组的最后结果（将数组拆分为不同的块）"""

# chunks=2的对称块————result: chunksize=(2, 2)
da_x1 = da.from_array(x, chunks=2)
"""
 0  1   2  3    4  5
 6  7   8  9    10 11
 
12 13   14 15   16 17
18 19   20 21   22 23

24 25   26 27   28 29
30 31   32 33   34 35
"""
# chunks=3的对称块————result: chunksize=(3, 3)
da_x2 = da.from_array(x, chunks=3)
"""
 0  1  2     3  4  5
 6  7  8     9 10 11
12 13 14    15 16 17

18 19 20    21 22 23
24 25 26    27 28 29
30 31 32    33 34 35
"""

# chunks=(3,2)的大小不对称但重复的块————result: chunksize=(3, 2)
da_x3 = da.from_array(x, chunks=(3, 2))
"""
 0  1    2  3    4  5
 6  7    8  9   10 11
12 13   14 15   16 17

18 19   20 21   22 23
24 25   26 27   28 29
30 31   32 33   34 35
"""
# chunks=(1,6)的大小不对称但重复的块————result: chunksize=(1, 6)
da_x4 = da.from_array(x, chunks=(1, 6))
"""
 0  1  2  3  4  5
 
 6  7  8  9 10 11
 
12 13 14 15 16 17

18 19 20 21 22 23

24 25 26 27 28 29

30 31 32 33 34 35
"""

# chunks=((2, 4), (3, 3))的非对称和不重复的块————result: chunksize=(4, 3)
da_x5 = da.from_array(x, chunks=((2, 4), (3, 3)))
"""
 0  1  2     3  4  5
 6  7  8     9 10 11
 
12 13 14    15 16 17
18 19 20    21 22 23
24 25 26    27 28 29
30 31 32    33 34 35
"""
# chunks=((2, 2, 1, 1), (3, 2, 1))的非对称和不重复的块————result: chunksize=(2, 3)
da_x6 = da.from_array(x, chunks=((2, 2, 1, 1), (3, 2, 1)))
"""
 0  1  2     3  4    5
 6  7  8     9 10   11
                    
12 13 14    15 16   17
18 19 20    21 22   23
                    
24 25 26    27 28   29
                    
30 31 32    33 34   35
"""

# 使用特殊值进行分块
da_x7 = da.from_array(x, chunks='auto')
da_x8 = da.from_array(x, chunks=(-1, 'auto'))
da_x9 = da.from_array(x, chunks={0: -1, 1: 'auto'})


print(da_x1)
print(da_x2)
print(da_x3)
print(da_x4)
print(da_x5)
print(da_x6)
print(da_x7)
print(da_x8)
print(da_x9)

# 查看配置值的块的大小
import dask
print(dask.config.get('array.chunk-size'))
