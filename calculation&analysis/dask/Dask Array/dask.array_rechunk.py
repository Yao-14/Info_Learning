"""
dask.array.rechunk(x[, chunks, threshold, ...])：将dask数组x中的块转换为新的块。

有时需要更改数据的分块布局。例如，也许涉及到你按行分块，但你需要做一个操作，如果跨列做的话要快得多。您可以使用rechunk方法更改组块。
"""
import dask.array as da
import numpy as np

x = da.from_array(np.random.randn(10000).reshape(100, 100), chunks=20)
print(x)    # chunksize=(20, 20)
x = x.rechunk(100)
print(x)    # chunksize=(100, 100)
x = x.rechunk((50, 100))
print(x)    # chunksize=(50, 100)
x = x.rechunk({0: 50, 1: 100})
print(x)    # chunksize=(50, 100)