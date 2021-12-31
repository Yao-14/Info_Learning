'''
方格热图——主要使用的模块：seaborn.heatmap
seaborn.heatmap(data, vmin=None, vmax=None, cmap=None, center=None, robust=False, annot=None, fmt='.2g',
                annot_kws=None, linewidths=0, linecolor='white', cbar=True, cbar_kws=None, cbar_ax=None,
                square=False, xticklabels='auto', yticklabels='auto', mask=None, ax=None, **kwargs)
data        :矩阵数据集，可以使numpy的数组（array）或pandas的dataframe。如果是pandas的dataframe，则df的index/column信息会直接对应到heatmap的columns和rows
vmax,vmin   :设置图例颜色带中最大值和最小值，没有该参数时默认不显示
cmap        :matplotlib颜色表名称或对象，或颜色列表，可选从数据值到色彩空间的映射。如果没有提供，默认设置
center      :将数据设置为图例中的均值数据，即图例中心的数据值；通过设置center值，可以调整生成的图像颜色的整体深浅；设置center数据时，如果有数据溢出，则手动设置的vmax、vmin会自动改变
robust      :如果“Ture”和“ vmin或” vmax不存在，则使用强分位数计算颜色映射范围，而不是极值。
annot       :如果为True，则将数据值写入每个单元格中，且数值注释默认显示的是科学记数法的数值。
annot_kws   :当annot=True时，可设置数值字体的大小，颜色，加粗，斜体字等。annot_kws={'size':9,'weight':'bold', 'color':'blue'}
fmt         :当annot=True时，设置数值的形式。fmt ='.0%'#显示百分比；fmt="d"显示整数形式；fmt ='f' ='g'显示完整数字；fmt ='.3f'显示小数的位数
linewidths  :间隔每个单元格的线的宽度。
linecolor   :间隔每个单元格的线的颜色。
cbar        :是否绘制颜色带图例，默认绘制
cbar_kws    :cbar_kws={ "orientation": "horizontal"}:设置为横向显示颜色带图例
square      :当square=True时，每一个单位格均为正方形
xticklabels :如果是True，则绘制dataframe的列名。如果是False，则不绘制列名。默认为True。
             如果是列表，则绘制列表中的内容作为xticklabels。
             如果是整数n，则绘制列名，但每个n绘制一个label。
yticklabels :如果是True，则绘制dataframe的行名。如果是False，则不绘制行名。默认为True。
             如果是列表，则绘制列表中的内容作为yticklabels。
             如果是整数n，则绘制列名，但每间隔n绘制一个label。
mask        :设置不显示的单元格。如mask=result<1，当result这个dataframe中小于1的数值不在热图上显示而是用空白显示。
ax          :设置绘制在哪一个子图上
'''
