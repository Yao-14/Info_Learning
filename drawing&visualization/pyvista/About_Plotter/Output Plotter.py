'''

************ 通过 pv.Plotter 输出 PNG 等图像文件的方法 ************
plotter.show(title='',                   ## 绘图窗口的标题
             interactive=True,           ## 在弹出交互界面时，是否允许用户平移和移动图形
             auto_close=False,           ## 在弹出交互界面时，是否在用户关闭窗口时退出绘图会话(建议一直设置False)
             window_size=[1024, 768]     ## 生成图像的大小
             screenshot='example.png',   ## 截取图像保存路径
             cpos='iso',                 ## 相机位置、焦点和向上视图的列表，用于设置截图的视角(可以自己设置列表，也可以使用以下几种特定视角）
                                            ('xy', 'xz', 'yz', 'yx', 'zx', 'zy', 'iso')
            )

************ 通过 pv.Plotter 输出 MP4 图像文件的方法 ************
## 第一步：在数据场景周围生成一条轨道路径。(factor指建立轨道范围时的缩放因子，factor越大图像越小(一般不用变)；
                                    n_points指轨道路径上的点数(一般不用变)；
                                    viewup指到轨道平面的法线(水平旋转为[0, 0, 1]，上下起伏旋转旋转为[0.5, 0.5, 1])。
                                    shift指将平面从场景中心向上/向下移动这个量(一般不用变)。
                                    )
path = plotter.generate_orbital_path(factor=3.0, viewup=[0, 0, 1], n_points=20, shift=0)
## 第二步：输出为 MP4 文件选择以下选项。(filename指输出mp4文件的文件名；
                                  framerate指每秒帧数，framerate越大旋转速度越快
                                  quality指任何编解码器质量，10最高，质量越高文件越大
                                  )
plotter.open_movie(filename, framerate=24, quality=5)
## 第三步：轨迹在给定的路径上聚焦焦点。(viewup指轨道平面的法线(一般不用变))
plotter.orbit_on_path(path, write_frames=True, viewup=[0, 0, 1], step=0.1)
## 第四步：关闭p对象
plotter.close()

************ 通过 pv.Plotter 输出 GIF 图像文件的方法 (与输出MP4类似) ************
path = plotter.generate_orbital_path(factor=3.0, viewup=[0, 0, 1], n_points=20, shift=0)
plotter.open_gif(filename)
plotter.orbit_on_path(path, write_frames=True, viewup=[0, 0, 1], step=0.1)
plotter.close()

'''

import pandas as pd
import pyvista as pv
data = pd.read_csv('D:\BGI\A_UsefulPackages\About 3D\PyVista\Example_Data\coordinate.csv')
points = data[['x','y','z']].values
grid = pv.PolyData(points)
volume = grid.delaunay_3d()

# 通过 pv.Plotter 绘制单一图像*********************************************************************************************
p1 = pv.Plotter(off_screen=True,
                shape=(1,1),
                border=True,
                border_color='white',
                multi_samples=8,
                line_smoothing=False,
                polygon_smoothing=False,
                lighting='light_kit')
p1.add_mesh(volume, show_scalar_bar=False, show_edges=False, opacity=0.5, color='gray')
p1.background_color = 'black'
p1.show(title='example plotter 1',
        interactive=True,
        auto_close=False,
        screenshot='Image\_Plotter1.png',
        cpos='iso')

# 通过 pv.Plotter 绘制多个图像*********************************************************************************************
p2 = pv.Plotter(off_screen=True,
                shape="3|1",
                border=True,
                border_color='white',
                multi_samples=8,
                lighting='light_kit')
for num, i in enumerate(['xy', 'xz', 'yz', 'iso']):
    p2.subplot(num)
    p2.add_mesh(volume, show_scalar_bar=False, show_edges=False, opacity=0.5, color='gray')
    p2.camera_position=i
p2.background_color = 'black'
p2.show(screenshot='Image\_Plotter2.png')

# 通过 pv.Plotter 绘制MP4图像*********************************************************************************************
p = pv.Plotter(off_screen=True)
p.add_mesh(volume, show_scalar_bar=False, show_edges=False, opacity=0.5,color='gray')
p.background_color = 'black'
path = p.generate_orbital_path(factor=3.0, shift=0, viewup=[0.5, 0.5, 1], n_points=20)
p.open_movie('Image\_Plotter3.mp4', framerate=10, quality=5)
p.orbit_on_path(path, write_frames=True, viewup=[0, 0, 1], step=0.1)
p.close()



