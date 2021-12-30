'''

PyTorch Version >= 1.8.0, 可使用以下函数在PyTorch上完成显存的使用上限设置，用户可以根据需要限制GPU的进程显存消耗上限。
                                        ————该方法对于一个用户一张显卡多个任务挺好的。
torch.cuda.set_per_process_memory_fraction(0.5, 0)
     参数1：fraction 限制的上限比例，如0.5 就是总GPU显存的一半，可以是0~1的任意float大小；
     参数2：device 设备号； 如0 表示GPU卡 0号；

'''

import torch
print(torch.cuda.is_available())
device = torch.cuda.device(0)
torch.cuda.set_per_process_memory_fraction(0.5,device=device)
total_memory = torch.cuda.get_device_properties(device).total_memory
# 设置显存使用上限是GPU总显存的50%，因此当使用60%时就会报错，如下所示
example_tensor1 = torch.empty(int(total_memory*0.3), dtype=torch.int8, device='cuda')
print(f'当前GPU中已使用的内存: {torch.cuda.memory_allocated(device=device) / 1024/1024} MB')