'''
************ 输出PNG等图像文件的主要方法 ************
1. 通过 .plot 直接绘图 (简易，绘制单一图使用，以下参数设置是个人推荐设置）
    DataSet.plot(off_screen=True,         ## 是否关闭弹出交互窗口(在集群、流程中等使用时建议True)
                 interactive = True,      ## 在弹出交互界面时，是否允许用户平移和移动图形
                 window_size=[1024, 768]  ## 生成图像的大小
                 screenshot='example.png',## 截取图像保存路径
                 cpos='iso',              ## 相机位置、焦点和向上视图的列表，用于设置截图的视角(可以自己设置列表，也可以使用以下几种特定视角）
                                             ('xy', 'xz', 'yz', 'yx', 'zx', 'zy', 'iso')
                 show_bounds=False,       ## 是否显示XYZ轴
                 show_axes=True,          ## 是否显示 vtk 轴小部件
                 background='black',      ## 设置背景颜色
                 text='',                 ## 在绘图底部添加文本
                 show_scalar_bar=False,   ## 是否展示颜色条
                 show_edges=False,        ## 是否显示边界
                 opacity=0.5,             ## 设置透明度
                 )

2. 通过 pv.Plotter 实现绘图 (专业，可同时绘制多个图），以下为最简单的流程
    plotter = pv.Plotter(off_screen=True,   ## 是否关闭弹出交互窗口(在集群、流程中等使用时建议True)
                         shape="3|1",       ## 绘制子图个数，指定方法有如下三种：
                                               shape=(2,2) 指定一个二乘二的网格绘制 4 个子图
                                               shape="3|1" 表示左侧有 3 个图，右侧有 1 个图 (个人认为最好)
                                               shape="4/2" 表示顶部有 4 个图，底部有 2 个图
                         window_size=[1024, 768]      ## 生成图像的大小
                         border=True,                 ## 是否在每个子图周围绘制边框
                         border_color='white',        ## 边框颜色
                         multi_samples=8,             ## 用于减少混叠的多个样本数(4是一个很好的默认值；但8会有更好的结果，对性能有潜在的影响)
                         line_smoothing=False,        ## 是否启用线条平滑
                         polygon_smoothing=False,     ## 是否启用多边形平滑
                         lighting='light_kit',        ## 设置照明强度('light_kit'(五灯), 'three lights'(三灯), 'none'(无灯))
                         )
    plotter.add_mesh(mesh, color='red')
    plotter.show(title='',                   ## 绘图窗口的标题
                 interactive=True,           ## 在弹出交互界面时，是否允许用户平移和移动图形
                 auto_close=False,           ## 在弹出交互界面时，是否在用户关闭窗口时退出绘图会话(建议一直设置False)
                 window_size=[1024, 768]     ## 生成图像的大小
                 screenshot='example.png',   ## 截取图像保存路径
                 cpos='iso',                 ## 相机位置、焦点和向上视图的列表，用于设置截图的视角(可以自己设置列表，也可以使用以下几种特定视角）
                                                ('xy', 'xz', 'yz', 'yx', 'zx', 'zy', 'iso')
                )
'''

import pandas as pd
import pyvista as pv
data = pd.read_csv('D:\BGI\A_UsefulPackages\About 3D\PyVista\Example_Data\coordinate.csv')
points = data[['x','y','z']].values
grid = pv.PolyData(points)
volume = grid.delaunay_3d()
# 通过 .plot 绘制单一图像**************************************************************************************************
volume.plot(off_screen=True,
            interactive = True,
            screenshot='Image\_plot.png',
            cpos='iso',
            show_bounds=False,
            show_axes=True,
            background='black',
            text='example of plot',
            show_scalar_bar=False,
            show_edges=False,
            opacity=0.5
            )
# 通过 pv.Plotter 绘制单一图像**********************************************************************************************
p1 = pv.Plotter(off_screen=True,
                shape=(1,1),
                border=True,
                border_color='white',
                multi_samples=8,
                line_smoothing=False,
                polygon_smoothing=False,
                lighting='light_kit')
p1.add_mesh(volume, show_scalar_bar=False, show_edges=False, opacity=0.8, color='white')
p1.background_color = 'black'
p1.show(title='example plotter 1',
        interactive=True,
        auto_close=False,
        screenshot='Image\_Plotter1.png',
        cpos='iso')

# 通过 pv.Plotter 绘制多个图像**********************************************************************************************
p2 = pv.Plotter(off_screen=True,
                shape="3|1",
                border=True,
                border_color='white',
                multi_samples=8,
                lighting='light_kit')
p2.subplot(0)
p2.add_mesh(volume, show_scalar_bar=False, show_edges=False, opacity=0.8, color='white')
p2.camera_position='xy'

p2.subplot(1)
p2.add_mesh(volume, show_scalar_bar=False, show_edges=False, opacity=0.8, color='lightskyblue')
p2.camera_position='xz'

p2.subplot(2)
p2.add_mesh(volume, show_scalar_bar=False, show_edges=False, opacity=0.8, color='orange')
p2.camera_position='yz'

p2.subplot(3)
p2.add_mesh(volume, show_scalar_bar=False, show_edges=False, opacity=0.8, color='red')
p2.camera_position='iso'

p2.background_color = 'black'
p2.show(screenshot='Image\_Plotter2.png')
