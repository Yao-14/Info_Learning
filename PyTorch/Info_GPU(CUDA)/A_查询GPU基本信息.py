
'''

******** 详细API查看 ********
https://pytorch.org/docs/master/cuda.html   英文
https://ptorch.com/docs/1/torch-cuda        中文（不全）

'''

import torch

# 查看PyTorch版本
torch_version = torch.version.__version__; print(f"PyTorch版本: {torch_version}")
# 查看CUDA版本
cuda_version = torch.version.cuda; print(f"CUDA版本: {cuda_version}")
# 查看PyTorch是否可以调用当前CUDA (True or False)
available = torch.cuda.is_available(); print(f"PyTorch是否可以调用当前CUDA: {available}")
# 查看PyTorch调用的CUDA是否初始化 (True or False)
torch.cuda.init()
initialized = torch.cuda.is_initialized(); print(f"PyTorch调用的CUDA是否初始化: {initialized}")
# 查看可用GPU的数量
deviceCount = torch.cuda.device_count(); print(f"可用GPU的数量: {deviceCount}")
# 查看所有GPU的名称，最后选择我们我们需要的GPU的index
for index in range(deviceCount):
    device = torch.cuda.device(index)
    device_name = torch.cuda.get_device_name(device=device)
    print("GPU", index, ":", device_name)
# 选择index为0的GPU（对于只有一个GPU的电脑，index永远等于0，设备索引默认从0开始）
device = torch.cuda.device(0)
# 获得该GPU的名字（即显卡名）
device_name = torch.cuda.get_device_name(device=device)
# 查看该GPU的计算能力（返回一个元组数据（major，minor），前者为主版本号，后者为次版本号————计算能力包括一个主版本号和一个次版本号，具有相同主版本号的设备具有相同的核心架构；次版本号对应于对核心架构的增量改进，可能包括新功能。）
device_capability = torch.cuda.get_device_capability(device=device) ; print(device_capability)
# 查看该GPU的主要属性（包括名字，主版本号，次版本号，总显存，总线程数）
device_propreties = torch.cuda.get_device_properties(device);print(device_propreties)
print(device_propreties.name,device_propreties.major,device_propreties.minor,device_propreties.total_memory,device_propreties.multi_processor_count)
# 查看当前选择的GPU的index
currect_device_index = torch.cuda.current_device(); print(currect_device_index)

