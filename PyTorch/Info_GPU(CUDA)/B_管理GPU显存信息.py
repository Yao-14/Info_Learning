
'''

******** 使用PyTorch检测GPU显存，而不使用pynvml的原因 ********
PyTorch使用缓存内存分配器来加速内存分配。因此，nvidia-smi所显示的值通常不会反映真实的内存使用情况。
PyTorch使用缓存内存分配器来加速内存分配。这允许在没有设备同步的情况下快速释放内存。但是，由分配器管理的未使用的内存仍将显示为在nvidia-smi中使用。您可以使用memory_allocated()和max_memory_allocated()监视张量占用的内存，并使用memory_cached()和 max_memory_cached()监视由缓存分配器管理的内存。调用empty_cache()可以从PyTorch释放所有未使用的缓存内存，以便其他GPU应用程序可以使用这些内存。但是，被张量占用的GPU内存不会被释放，因此它不能增加PyTorch可用的GPU内存量。

******** 详细API查看 ********
https://pytorch.org/docs/master/cuda.html   英文
https://ptorch.com/docs/1/torch-cuda        中文（不全）

******** Memory management ********
1、torch.cuda.empty_cache()
    释放当前由caching allocator保存的所有未占用的缓存内存，以便可以在其他GPU应用程序中使用这些缓存并在nvidia-smi中可见。

2、torch.cuda.memory_allocated(device=None)
    返回参数设备的张量占用的当前GPU内存（以字节为单位）。这可能小于nvidia-smi中显示的数量，因为缓存分配器可以保留一些未使用的内存，并且需要在GPU上创建一些上下文。

3、torch.cuda.max_memory_allocated(device=None)
    返回参数设备的张量占用的最大GPU内存（以字节为单位）。
    默认情况下，这将返回自此程序开始以来的峰值分配内存。 reset_max_memory_allocated（）可用于重置跟踪此度量标准的起点。例如，这两个函数可以测量训练循环中每次迭代的峰值分配内存使用量。

4、torch.cuda.reset_max_memory_allocated(device=None)
    重置跟踪参数设备的张量占用的最大GPU内存的起点。

5、torch.cuda.memory_reserved(device=None)
    返回由缓存分配器管理的当前GPU内存（以字节为单位）。

6、torch.cuda.max_memory_reserved(device=None)
    返回给定设备的缓存分配器管理的最大GPU内存（以字节为单位）
    默认情况下，这将返回自此程序开始以来的峰值缓存内存。reset_max_memory_cached（）可用于重置跟踪此指标的起点。例如，这两个函数可以测量训练循环中每次迭代的峰值缓存内存量。

7、torch.cuda.reset_max_memory_cached(device=None)
    重置跟踪给定设备的高速缓存分配器管理的最大GPU内存的起点。

'''

import torch

# 查看PyTorch是否可以调用当前CUDA (True or False)
available = torch.cuda.is_available() ; print(f"PyTorch是否可以调用当前CUDA: {available}")
# 选择index为0的GPU（对于只有一个GPU的电脑，index永远等于0，设备索引默认从0开始）
device = torch.cuda.device(0)
# 查看该GPU的总显存(这里是字节bytes，所以要想得到以兆M为单位就需要除以1024**2)
M = 1024*1024 ; G = 1024*M
total_memory = torch.cuda.get_device_properties(device).total_memory ; print(f"GPU总显存: {int(total_memory/G)} GB ({int(total_memory/M)} MB)")
# 查看当前GPU中已使用的内存（以字节为单位）
allocated_memory = torch.cuda.memory_allocated(device=device); print(f'当前GPU中已使用的内存: {int(allocated_memory/M)} MB')
# 查看当前由缓存分配器管理的GPU内存（略大于已使用的内存，因为缓存分配器可以保留一些未使用的内存）
reserved_memory = torch.cuda.memory_reserved(device=device);   print(f'当前由缓存分配器管理的GPU内存: {int(reserved_memory/M)} MB')
# 清空缓存（即清空缓存分配器保留的一些未使用的内存）
torch.cuda.empty_cache()
# 清空已使用的内存 ---- 通过 del 矩阵，使用如下
example_tensor1 = torch.empty(int(total_memory*0.5), dtype=torch.int8, device='cuda')
example_tensor2 = torch.empty(int(total_memory*0.2), dtype=torch.int8, device='cuda')
print(f'当前GPU中已使用的内存: {torch.cuda.memory_allocated(device=device) / M} MB')
del example_tensor1 ; print(f'当前GPU中已使用的内存: {torch.cuda.memory_allocated(device=device) / M} MB')
del example_tensor2 ; print(f'当前GPU中已使用的内存: {torch.cuda.memory_allocated(device=device) / M} MB')