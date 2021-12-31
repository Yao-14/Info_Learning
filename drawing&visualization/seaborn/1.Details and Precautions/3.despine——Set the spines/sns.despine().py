'''
sns.despine(fig=None, ax=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)
设置边框
fig：选择图表
ax：选择子图
top, right, left, bottom:True or False。若为True则移除这一边的边框。默认情况下移除top和right。
offset：设置两坐标轴离开距离
trim：True or False。若为True，当边框没有覆盖整个数据轴的范围的时候，trim参数会限制留存的边框范围。
'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_context(context='notebook', font_scale=1, rc={'font.size': 20.0})
data = pd.DataFrame([[1,2,3,4],[1,2,3,4],[1,2,3,4]],index=['AA','BB','CC'],columns=['fi','se','th','fo'])
sns.barplot(data=data)
sns.despine(top=True, right=True,offset=10,trim=True)
plt.savefig('test.pdf')
