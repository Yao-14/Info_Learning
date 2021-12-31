
import torch

torch.cuda.init()
# 选择编号为0的GPU
device = torch.cuda.device(0)

M = 1024*1024
G = 1024*1024*1024
# 查看GPU总显存
total_memory = torch.cuda.get_device_properties(device).total_memory
print(f"GPU的总显存: {int(total_memory/G)} GB ({int(total_memory/M)} MB)")

# 设置显存使用上限，当显存使用超过上限时就会报错(0.8表示上限为总显存的80%) ———— 该方法对于一个用户一张显卡多个任务挺好的
torch.cuda.set_per_process_memory_fraction(0.8, device=device)

# 创建两个tnesor占用GPU部分显存
example_tensor1 = torch.empty(int(total_memory*0.5), dtype=torch.int8, device='cuda')
example_tensor2 = torch.empty(int(total_memory*0.2), dtype=torch.int8, device='cuda')

# 查看GPU中已使用显存
allocated_memory = torch.cuda.memory_allocated(device=device)
print(f'GPU已使用显存: {round(allocated_memory/G, 2)} GB ({round(allocated_memory/M, 2)} MB)')

# 查看当前由缓存分配器管理的GPU显存（略大于已使用的显存，因为缓存分配器可以保留一些未使用的显存）
reserved_memory = torch.cuda.memory_reserved(device=device)
print(f'GPU中由缓存分配器管理的显存: {round(reserved_memory/G, 2)} GB ({round(reserved_memory/M, 2)} MB)')

# 清空缓存（即清空缓存分配器保留的一些未使用的显存）
torch.cuda.empty_cache()

# 清空已使用的显存 ---- 通过 del
del example_tensor1
allocated_memory = torch.cuda.memory_allocated(device=device)
print(f'清空 example_tensor1 使用的内存后GPU已使用显存: {round(allocated_memory/G, 2)} GB ({round(allocated_memory/M, 2)} MB)')