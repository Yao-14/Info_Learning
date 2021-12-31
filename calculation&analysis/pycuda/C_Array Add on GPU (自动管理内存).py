'''

对于一般运算，需要手动编写核函数，而后通过核函数在 GPU 环境下运行gpuarray数据。

************ CPU 数据和 GPU 数据之间的传输转换方法 ---- gpuarray.to_gpu() ************
    import pycuda.autoinit
    import pycuda.gpuarray as gpuarray
    gpu_array = gpuarray.to_gpu( cpu_array )
    # 注意事项：进行转换的时候应该尽可能通过 numpy.dtype 指定 cpu_array 的数据类型，以避免不必要的性能损失。
    # gpuarray方法是自动分配显存空间

************ Kernel(核函数） ----  ************
    from pycuda.compiler import SourceModule
    mod = SourceModule(r"""void __global__ 核函数名(参数1, 参数2,...)
                            {
                            计算过程
                            }
                        """)
    kernel = mod.get_function("核函数名")

************ CUDA核函数的线程组织 ---- 网格（grid）、块（block）与线程（thread） ************
    核心关系：一个单独的 Kernel 启动一个 grid，grid 可以是一维、二维或者三维。
            一个 gird 由 n 个 block 组成，block 可以是一维、二维或者三维。
            一个 block 由 n 个thread 组成 （grid 中所有 thread 共享 global memory）

    PyCuda 中 grid 的参数（以二维 grid 为例）：
            gridDim.x: grid 的 x 方向的维度（即 x 方向的 block 数量） ----gridDim.x = 5，即 grid 每行有5个 block。
            gridDim.y: grid 的 y 方向的维度（即 y 方向的 block 数量） ----gridDim.y = 3，即 grid 每列有3个 block。
    PyCuda 中 block 的参数以二维 block 为例）：
            blockDim.x: block的x方向的维度（即x方向的线程数量） ---- blockDim.x = 5，即 block 每行有5个线程。
            blockDim.y: block的y方向的维度（即y方向的线程数量） ---- blockDim.y = 3，即 block 每列有3个线程。
            blockIdx.x: block在x方向的位置（索引）---- blockIdx.x，即 block 在该 grid 行方向的的2号位置。（从0开始排位，即 blockIdx = [0, 1, 2, ...])
            blockIdx.y: block在y方向的位置（索引）---- blockIdx.y，即 block 在该 grid 列方向的的2号位置。（从0开始排位，即 blockIdx = [0, 1, 2, ...])
    PyCuda 中 thread 的参数以二维 thread 为例）：
            threadIdx.x: thread在x方向的位置（索引）---- threadIdx.x = 2，即 thread 在该 block 行方向的的2号位置。（从0开始排位，即 threadIdx = [0, 1, 2, ...])
            threadIdx.y: thread在y方向的位置（索引）---- threadIdx.y = 2，即 thread 在该 block 列方向的的2号位置。（从0开始排位，即 threadIdx = [0, 1, 2, ...])
    # 注意事项：数据在GPU中按照行优先排列

************ PyCuda核函数中grid和block的设置 ---- grid=(num1, num2, num3), block=(num1, num2, num3) ************
    grid = (num1, num2, num3)   ---- grid参数格式上可以省略后两个参数，但是num后面的逗号不能省略。
    block = (num1, num2, num3)  ---- block参数的格式必须是一个长度为3元组，而且元组元素的类型为int。



************ 从GPU下载 gpuarray 数据到CPU的方法 ---- get()接口 ************
    cpu_array_new = gpu_array.get()

'''
import pycuda.autoinit
from pycuda.compiler import SourceModule
import pycuda.gpuarray as gpuarray
import numpy
import warnings
warnings.filterwarnings('ignore')

'''************ Example1 ---- grid, block, thread 索引关系 ************'''
mod1 = SourceModule(r"""__global__ void print_id(void)
                        {
                            printf("blockIdx.x = %d; blockIdx.y = %d; blockIdx.z = %d; threadIdx.x = %d; threadIdx.y = %d; threadIdx.z = %d;\n", 
                                    blockIdx.x, blockIdx.y, blockIdx.z, threadIdx.x, threadIdx.y, threadIdx.z);
                        }
                        """)

print_id = mod1.get_function("print_id")
# 一维
#print_id(grid=(2,1,1), block=(3,1,1)) # 创建了一个1行2列的grid，包含2个block。
                                      # 创建的每个block是一行三列的，每个block包含3个thread
# 二维
print_id(grid=(2,2,1), block=(3,2,1)) # 创建了一个2行2列的grid，包含4个block。
                                      # 创建的每个block是两行三列的，每个block包含6个thread
# 三维
#print_id(grid=(2,2,2), block=(3,2,2)) # 创建了一个2行2列2纵的grid，包含8个block。
                                      # 创建的每个block是两行三列两纵的，每个block包含12个thread。

'''************ Example2 ---- 对于一维的grid和block的一个一般运算 ************'''

mod = SourceModule(r"""
void __global__ add(const float *x, const float *y, float *z)
{
    const int n = blockDim.x * blockIdx.x + threadIdx.x;
    z[n] = x[n] + y[n];
    printf("blockDim.x = %d; blockIdx.x = %d; threadIdx.x = %d; n = %d;\n", blockDim.x, blockIdx.x, threadIdx.x,n);
}
""")
add = mod.get_function("add")
num = 6
A = numpy.random.rand(num)
B = numpy.random.rand(num)
C = numpy.zeros(num)
A_GPU = gpuarray.to_gpu(A.astype(numpy.float32))
B_GPU = gpuarray.to_gpu(B.astype(numpy.float32))
C_GPU = gpuarray.to_gpu(B.astype(numpy.float32))
add(A_GPU, B_GPU, C_GPU, grid=(2,), block=(3,1,1))
C = C_GPU.get()
print('A=', A)
print('B=', B)
print('C=', C)