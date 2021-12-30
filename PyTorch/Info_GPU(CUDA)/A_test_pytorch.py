'''
Test whether the installation is successful pytorch.
'''

import torch

# 查看PyTorch版本
print(f"PyTorch版本: {torch.version.__version__}")

# 查看CUDA版本
print(f"CUDA版本: { torch.version.cuda}")

# 查看PyTorch是否可以调用当前CUDA (True or False)
print(f"PyTorch是否可以调用当前CUDA: {torch.cuda.is_available()}")

# 查看PyTorch调用的CUDA是否初始化 (True or False)
torch.cuda.init()
print(f"PyTorch调用的CUDA是否初始化: { torch.cuda.is_initialized()}")

# 查看可用GPU的数量、编号及名字
device_count = torch.cuda.device_count()
for i in range(device_count):
    device = torch.cuda.device(i)
    device_name = torch.cuda.get_device_name(device=device)
    print(f"编号为 {i} 的GPU是 {device_name}")
print(f"可使用的GPU数量共计{device_count}个")
