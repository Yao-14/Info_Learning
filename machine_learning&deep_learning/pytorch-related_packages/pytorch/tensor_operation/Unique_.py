'''
torch.unique()  返回输入张量的唯一元素。（输出元素默认会按升序进行排序）

参数：input (Tensor)   输入张量
     sorted (bool)    默认值：True。在作为输出返回之前是否按升序对唯一元素进行排序
     return_inverse (bool)  默认值：False。是否还返回原始输入中元素在返回的唯一列表中的位置的索引
     return_counts (bool)   默认值：False。是否还返回每个唯一元素的计数
     dim (int)  默认值：None。应用唯一的维度。如果None，则返回扁平输入的唯一值。
                若dim=0，以二维数组为例，则返回唯一行
                若dim=1，以二维数组为例，则返回唯一列


torch.unique_consecutive()  从每个连续的等效元素组中消除除第一个元素之外的所有元素。
                            (对于[1,2,3,2]返回[1,2,3,2]；对于[1,2,2,3]则返回[1,2,3])
input (Tensor)   输入张量
return_inverse (bool)  默认值：False。是否还返回原始输入中元素在返回的唯一列表中的位置的索引
return_counts (bool)   默认值：False。是否还返回每个唯一元素的计数
dim (int)  默认值：None。应用唯一的维度。如果None，则返回扁平输入的唯一值。
           若dim=0，以二维数组为例，则返回唯一行
           若dim=1，以二维数组为例，则返回唯一列
'''

import torch
'''******** torch.unique() ********'''
example_tensor = torch.tensor([[1, 5, 5, 2, 3, 1, 5, 4, 5, 5],[5, 3, 3, 1, 4, 4, 2, 1, 5, 5],[5, 3, 3, 1, 4, 4, 2, 1, 5, 5]], dtype=torch.long)
u_example1 = torch.unique(example_tensor)
u_example2 ,u_index2 = torch.unique(example_tensor,return_inverse=True)
u_example3,u_counts3 = torch.unique(example_tensor,return_counts=True)
u_example4 = torch.unique(example_tensor,dim=0)
print(u_example1)
print(u_example2, u_index2)
print(u_example3,u_counts3)
print(u_example4)

'''******** torch.unique_consecutive() ********'''
uc_example1 = torch.unique_consecutive(example_tensor)
print(uc_example1)