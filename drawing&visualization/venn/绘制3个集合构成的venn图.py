from venn import venn
import matplotlib.pyplot as plt

#准备三个数据集合
set1 = set([1,2,3,4,5,6,7,8])
set2 = set([5,6,7,8,9,10,11,12])
set3 = set([1,3,5,7,9,11,13,15])
#将所有集合放到一个字典中并对每一个集合命名
dataall = {
    "set1": set1,
    "set2": set2,
    "set3": set3}
#绘制venn图
venn(dataall)
plt.show()