
'''
bbox： 给字体添加框,如 bbox=dict(boxstyle='Circos',facecolor='red', alpha=0.5)
'''

import matplotlib.pyplot as plt
import matplotlib.patches as mpatch

styles = mpatch.BoxStyle.get_styles()
spacing = 1.2

figheight = (spacing * len(styles) + .5)
fig = plt.figure(figsize=(4 / 1.5, figheight / 1.5))
fontsize = 0.3 * 72

for i, stylename in enumerate(sorted(styles)):
    fig.text(0.5, (spacing * (len(styles) - i) - 0.5) / figheight, stylename,
             ha="center",
             size=fontsize,
             bbox=dict(boxstyle=stylename, fc="w", ec="k"))
plt.show()