'''
sns.set_theme()集合了set_style、set_context等用于一次性设置context, style, palette等属性:
    sns.set_theme(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)

sns.set_theme()中的参数包括：
context：主要用于设置图表内各元素的样式,seaborn内置的样式包括'notebook','paper','talk','poster'四种
style：主要用于设置图表本身样式,seaborn内置的样式包括'darkgrid','whitegrid','dark','white','ticks'五种
    若要自己修改style属性中的部分值，可以通过set_style
{'figure.facecolor': 'white', 'axes.labelcolor': '.15', 'xtick.direction': 'out', 'ytick.direction': 'out', 'xtick.color': '.15', 'ytick.color': '.15', 'axes.axisbelow': True, 'grid.linestyle': '-', 'text.color': '.15', 'font.family': ['sans-serif'], 'font.sans-serif': ['Arial', 'DejaVu Sans', 'Liberation Sans', 'Bitstream Vera Sans', 'sans-serif'], 'lines.solid_capstyle': 'round', 'patch.edgecolor': 'w', 'patch.force_edgecolor': True, 'image.cmap': 'rocket', 'xtick.top': False, 'ytick.right': False, 'axes.grid': False, 'axes.facecolor': 'white', 'axes.edgecolor': '.15', 'grid.color': '.8', 'axes.spines.left': True, 'axes.spines.bottom': True, 'axes.spines.right': True, 'axes.spines.top': True, 'xtick.bottom': False, 'ytick.left': False}

palette：主要用于设置调色盘，查看palette即可
font：设置字体
font_scale：设置字体元素的大小
color_codes：True or False.
'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_theme(context='poster',style='whitegrid',
              font='Arial',font_scale=1,
              palette='Accent')
data = pd.DataFrame([[1,2,3,4],[1,2,3,4],[1,2,3,4]],index=['AA','BB','CC'],columns=['fi','se','th','fo'])
sns.barplot(data=data)
plt.savefig('test.pdf')