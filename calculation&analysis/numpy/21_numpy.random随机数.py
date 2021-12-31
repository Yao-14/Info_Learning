
from numpy import random

# numpy.random.uniform(low=0.0, high=1.0, size=None)
# 生出size个符合标准正态分布的浮点数，取值范围为[low, high)，默认取值范围为[0, 1.0)
print(random.uniform(3, 6, size=6))
print(random.uniform(3, 6, size=(2, 3)))

# numpy.random.randint(low, high=None, size=None, dtype='I')
# 生成size个整数，取值区间为[low, high)，若没有输入参数high则取值区间为[0, low),左闭右开
print(random.randint(3, 6, size=6))
print(random.randint(3, 6, size=(2, 3)))

# numpy.random.rand(d0, d1, ..., dn)
# 生成一个(d0, d1, ..., dn)维的数组，数组的元素取自[0, 1)上的标准正态分布，若没有参数输入, 左闭右闭
print(random.rand(3))
print(random.rand(2,3))
print(random.rand(2,3,2))

# numpy.random.random(size=None)
# 生成[0.0, 1.0)之间的浮点数
print(random.random(size=6))
print(random.random(size=(2,3)))