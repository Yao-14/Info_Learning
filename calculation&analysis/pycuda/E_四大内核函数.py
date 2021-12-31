'''

pycuda.elementwise.ElementwiseKernel (Python class, in GPU Arrays)

pycuda.reduction.ReductionKernel (Python class, in GPU Arrays)

pycuda.scan.ExclusiveScanKernel (Python class, in GPU Arrays)

pycuda.scan.InclusiveScanKernel (Python class, in GPU Arrays)

'''
import pycuda.autoinit
import pycuda.gpuarray as gpuarray
from pycuda.curandom import rand as curand
from pycuda.elementwise import ElementwiseKernel
a_gpu = curand((50,))
b_gpu = curand((50,))
lin_comb = ElementwiseKernel(
        "float a, float *x, float b, float *y, float *z",
        "z[i] = a*x[i] + b*y[i]",
        "linear_combination")

c_gpu = gpuarray.empty_like(a_gpu)
lin_comb(5, a_gpu, 6, b_gpu, c_gpu)
print(c_gpu)
