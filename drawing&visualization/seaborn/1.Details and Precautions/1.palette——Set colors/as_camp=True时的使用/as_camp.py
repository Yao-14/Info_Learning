import matplotlib.pyplot as plt
import seaborn as sns

#颜色设置——调色盘
cmap = sns.color_palette(palette='Greens')
print(cmap)
list1 = [1, 1, 1, 1, 2, 3, 2, 2, 2, 1, 3, 4, 5, 7, 1, 1, 3, 4, 6, 2]
list2 = [3,2,4,8,6,1,3,5,1,0,6,2,9,6,4,1,2,7,3,2]
sns.kdeplot(x=list1,y=list2, shade=True,cmap=cmap,cbar=True,bw_adjust=1.2)
plt.show()
