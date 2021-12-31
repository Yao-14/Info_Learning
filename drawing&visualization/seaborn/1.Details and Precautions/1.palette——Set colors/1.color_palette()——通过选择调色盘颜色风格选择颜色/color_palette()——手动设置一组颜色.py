'''
color_palette()不仅可以接受特定的颜色风格，也可以手动设置一组需要的颜色。color_palette()函数会接受一个颜色列表
'''
import matplotlib.pyplot as plt
import seaborn as sns

flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
sns.palplot(sns.color_palette(flatui))
plt.show()