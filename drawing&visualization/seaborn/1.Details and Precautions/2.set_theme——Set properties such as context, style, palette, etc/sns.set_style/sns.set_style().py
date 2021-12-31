'''
sns.set_style(style='',rc={}):
style:seaborn内置的样式包括'darkgrid','whitegrid','dark','white','ticks'五种
若要自己修改style属性中的部分值，通过rc={}修改，可修改的参数如下：
    {'figure.facecolor': 'white', 'axes.labelcolor': '.15', 'xtick.direction': 'out', 'ytick.direction': 'out',
    'xtick.color': '.15', 'ytick.color': '.15', 'axes.axisbelow': True, 'grid.linestyle': '-', 'text.color': '.15',
    'font.family': ['sans-serif'], 'font.sans-serif': ['Arial', 'DejaVu Sans', 'Liberation Sans', 'Bitstream Vera Sans',
    'sans-serif'], 'lines.solid_capstyle': 'round', 'patch.edgecolor': 'w', 'patch.force_edgecolor': True,
    'image.cmap': 'rocket', 'xtick.top': False, 'ytick.right': False, 'axes.grid': False, 'axes.facecolor': 'white',
    'axes.edgecolor': '.15', 'grid.color': '.8', 'axes.spines.left': True, 'axes.spines.bottom': True, 'axes.spines.right': True,
    'axes.spines.top': True, 'xtick.bottom': False, 'ytick.left': False}
'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_style(style='darkgrid',rc={'figure.facecolor': 'grey'})
data = pd.DataFrame([[1,2,3,4],[1,2,3,4],[1,2,3,4]],index=['AA','BB','CC'],columns=['fi','se','th','fo'])
sns.barplot(data=data)
plt.savefig('test.pdf')