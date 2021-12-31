from venn import venn
import matplotlib.pyplot as plt

#准备两个数据集合
set1 = set([1,2,3,4,5,6,7,8])
set2 = set([5,6,7,8,9,10,11,12])
#将所有集合放到一个字典中并对每一个集合命名
dataall = {
    "set1": set(set1),
    "set2": set(set2)}
#绘制venn图
venn(dataall)
plt.show()