'''

对于最简易的一些运算（加减乘除），只需将在 CPU 环境运行的NumPy array数据转换为在 GPU 环境运行的gpuarray数据即可进行运算。

************ CPU 数据和 GPU 数据之间的传输转换方法 ---- gpuarray.to_gpu() ************
import pycuda.autoinit
import pycuda.gpuarray as gpuarray
gpu_array = gpuarray.to_gpu( cpu_array )
# 注意事项：进行转换的时候应该尽可能通过 numpy.dtype 指定 cpu_array 的数据类型，以避免不必要的性能损失。
# gpuarray方法是自动分配显存空间

************ 从GPU下载 gpuarray 数据到CPU的方法 ---- get()接口 ************
cpu_array_new = gpu_array.get()

'''

import pycuda.autoinit
import pycuda.gpuarray as gpuarray
import numpy as np
from time import time
import warnings
warnings.filterwarnings('ignore')
'''************ Example ---- 简易运算比较CPU和GPU性能 ************'''
def simple_speed_test(n):
    host_data = np.float32(np.random.random(5000000000)).astype(np.float32)

    t1 = time()
    host_data_2x = host_data * np.float32(n)
    t2 = time()

    print(f'total time to compute on CPU: {t2 - t1}')

    device_data = gpuarray.to_gpu(host_data)

    t3 = time()
    device_data_2x = device_data * np.float32(n)
    t4 = time()

    from_device = device_data_2x.get()

    print(f'total time to compute on GPU: {t4 - t3}')
    print(f'Is the host computation the same as the GPU computation? : {np.allclose(from_device, host_data_2x)}')

simple_speed_test(n=2)
simple_speed_test(n=4)
simple_speed_test(n=6)