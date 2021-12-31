'''
seaborn.set_context(context='notebook', font_scale=1, rc={}):

context:seaborn内置的样式包括'notebook','paper','talk','poster'
font_scale：设置字体元素的大小
若要自己修改context属性中的部分值，通过rc={}修改，可修改的参数如下：
    {'font.size': 24.0, 'axes.labelsize': 24.0, 'axes.titlesize': 24.0, 'xtick.labelsize': 22.0, 'ytick.labelsize': 22.0,
    'legend.fontsize': 22.0, 'axes.linewidth': 2.5, 'grid.linewidth': 2.0, 'lines.linewidth': 3.0, 'lines.markersize': 12.0,
    'patch.linewidth': 2.0, 'xtick.major.width': 2.5, 'ytick.major.width': 2.5, 'xtick.minor.width': 2.0,
    'ytick.minor.width': 2.0, 'xtick.major.size': 12.0, 'ytick.major.size': 12.0, 'xtick.minor.size': 8.0,
    'ytick.minor.size': 8.0, 'legend.title_fontsize': 24.0}
'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_context(context='notebook', font_scale=2, rc={'font.size': 20.0})
data = pd.DataFrame([[1,2,3,4],[1,2,3,4],[1,2,3,4]],index=['AA','BB','CC'],columns=['fi','se','th','fo'])
sns.barplot(data=data)
plt.savefig('test.pdf')