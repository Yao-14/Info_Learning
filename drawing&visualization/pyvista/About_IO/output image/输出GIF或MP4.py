'''

************ 输出GIF或MP4文件的主要方法 ************
p = pv.Plotter()
p.add_mesh()
## 第一步：在数据场景周围生成一条轨道路径。(factor指建立轨道范围时的缩放因子，factor越大图像越小(一般不用变)；
                                    n_points指轨道路径上的点数(一般不用变)；
                                    viewup指到轨道平面的法线(水平旋转为[0, 0, 1]，上下起伏旋转旋转为[0.5, 0.5, 1])。
                                    shift指将平面从场景中心向上/向下移动这个量(一般不用变)。
path = p.generate_orbital_path(factor=3.0, viewup=[0, 0, 1], n_points=20, shift=0)
## 第二步：输出为 GIF 文件选择以下选项。(filename指输出gif文件的文件名)
p.open_gif(filename)
## 第二步：输出为 MP4 文件选择以下选项。(filename指输出mp4文件的文件名；
                                  framerate指每秒帧数，framerate越大旋转速度越快
                                  quality指任何编解码器质量，10最高，质量越高文件越大
                                  )
p.open_movie(filename, framerate=24, quality=5)
## 第三步：轨迹在给定的路径上聚焦焦点。(viewup指轨道平面的法线(一般不用变))
p.orbit_on_path(path, write_frames=True, viewup=[0, 0, 1], step=0.1)
## 第四步：关闭p对象
p.close()

'''

import pandas as pd
import pyvista as pv
data = pd.read_csv('D:\BGI\A_UsefulPackages\About 3D\PyVista\Example_Data\coordinate.csv')
points = data[['x','y','z']].values
grid = pv.PolyData(points)
volume = grid.delaunay_3d()

p = pv.Plotter(off_screen=True,)
p.add_mesh(volume, show_scalar_bar=False, show_edges=False, opacity=0.5,color='white')
p.background_color = 'black'
# 输出为GIF文件 **********************************************************************************************************
path = p.generate_orbital_path(factor=3.0, shift=0, viewup=[0.5, 0.5, 1], n_points=20)
p.open_movie('Image\_GIF.mp4', framerate=10, quality=5)
p.orbit_on_path(path, write_frames=True, viewup=[0, 0, 1], step=0.1)
p.close()



