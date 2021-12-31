'''

************ PyCuda基本使用流程 ************
第一步：    初始化PyCUDA模块（一般自动初始化即导入 import pycuda.autoinit ---- 必须要有）
第二步：    输入Array数组数据
第三步：    导入一个用于编译的类，构造一个类对象（编译CUDA代码，使之成为可以被执行的GPU程序）。
第四步：    从类对象中获得一个函数的执行入口。
第五步：    通过这个入口，执行GPU程序。
'''

'''************ Example ************'''
import warnings
warnings.filterwarnings('ignore')
# 初始化PyCUDA模块
import pycuda.autoinit
# 导入一个用于编译的类
from pycuda.compiler import SourceModule
# 构造一个类对象
mod = SourceModule( r"""
                    __global__ void hello_from_gpu(void)
                    {
                        printf("Hello World from the GPU!\n");
                    }
                    """)
# 从类对象中获得一个函数的执行入口
hello_from_gpu = mod.get_function("hello_from_gpu")
# 通过这个入口，执行GPU程序
hello_from_gpu(block=(3,2,2))