'''
View the basic information of a GPU, take the GPU numbered 0 (the default GPU) as an example:
'''

import torch

# 查看PyTorch是否可以调用当前CUDA (True or False)
print(f"PyTorch是否可以调用当前CUDA: {torch.cuda.is_available()}")

# 查看PyTorch调用的CUDA是否初始化 (True or False)
torch.cuda.init()
print(f"PyTorch调用的CUDA是否初始化: { torch.cuda.is_initialized()}")

# 选择编号为0的GPU
device = torch.cuda.device(0)

# 查看当前选择的GPU的编号
print(f"GPU的编号: {torch.cuda.current_device()}")

M = 1024*1024
G = 1024*1024*1024
# 查看该GPU的主要属性（包括名字，主版本号，次版本号，总显存，总线程数）
device_propreties = torch.cuda.get_device_properties(device)
print(f"GPU的名字: {device_propreties.name}")
print(f"GPU的计算能力: {device_propreties.major}.{device_propreties.minor}")
print(f"GPU的总显存: {int(device_propreties.total_memory/G)} GB ({int(device_propreties.total_memory/M)} MB)")
print(f"GPU的总线程数: {device_propreties.multi_processor_count}")

# 查看GPU中已使用显存
allocated_memory = torch.cuda.memory_allocated(device=device)
print(f'GPU已使用显存: {round(allocated_memory/G, 2)} GB ({round(allocated_memory/M, 2)} MB)')

# 查看当前由缓存分配器管理的GPU内存（略大于已使用的内存，因为缓存分配器可以保留一些未使用的内存）
reserved_memory = torch.cuda.memory_reserved(device=device)
print(f'GPU中由缓存分配器管理的显存: {round(reserved_memory/G, 2)} GB ({round(reserved_memory/M, 2)} MB)')