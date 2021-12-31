'''

************ 通过点云数据 (point cloud) 重构其表面的方法 ************
1. 三维层面：
    (1). pyvista.DataSetFilters.reconstruct_surface()   # 不太好用（surf = grid.reconstruct_surface()）
    (2). DataSetFilters.delaunay_3d()                   # 推荐使用
2. 二维层面：
    (1). DataSetFilters.delaunay_2d()

************ 提取重构体表面的方法 ************
1. 提取表面
    pv.DataSetFilters.extract_surface()
2. 只提取外表面
    pv.DataSetFilters.extract_geometry()

************ 重构表面平滑化的方法 ************
1. 应用 Laplacian平滑算法 平滑化表面
    pv.PolyData.smooth(n_iter=100)         # 应用平滑过滤器通过Laplacian平滑算法平滑化外表面
                                           (n_iter表示Laplacian平滑算法的迭代次数，迭代次数越大，表面越平滑)
2. 通过 细分表面 平滑化表面
    pv.PolyDataFilters.subdivide(nsub=3, subfilter='loop')  # 增加单个连接的三角形网格中的三角形数量,从而细分表面使表面更平滑
                                                            (nsub表示细分数，nsub越大细分越多)
                                                            (subfilter表示细分表面网络的算法，包括'linear','butterfly','loop'，
                                                            推荐使用'butterfly'和'loop'， 最推荐'loop')
************ 使用表面网格剪裁任何网格类型 ************
1. 使用pyvista.PolyData表面网格剪裁任何网格类型。
    PolyDataFilters.clip_surface(surface)



'''
import pandas as pd
import pyvista as pv

# 输入点云数据 ************************************************************************************************************
data = pd.read_csv('..\Example_Data\coordinate.csv')
points = data[['x','y','z']].values
grid = pv.PolyData(points)
grid["cluster"] = data["cluster"]
# 重构表面 ***************************************************************************************************************
volume = grid.delaunay_3d()

# 提取重构体表面 **********************************************************************************************************
## 提取表面
'''surf = volume.extract_surface(nonlinear_subdivision=5)'''
## 提取外表面
surf = volume.extract_geometry()

# 平滑化表面(一般以下两种方法二选一即可) **************************************************************************************
## 应用 Laplacian平滑算法 平滑化表面
surf.smooth(n_iter=10, inplace=True)
## 通过 细分表面 平滑化表面
surf.subdivide(nsub=3, subfilter="loop", inplace=True)

# 裁剪原始点云适配平滑化后的表面 *********************************************************************************************
clipped = grid.clip_surface(surf)

# 可视化模型并保存 ********************************************************************************************************

## 可视化表面
surf.plot(show_scalar_bar=False, show_edges=True, opacity=0.5, line_width=1,interactive=False,
          color=True, screenshot='Image\surface_reconstruction_surface.png')

## 可视化表面点云
surf_points = pv.PolyData(surf.points)
surf_points.plot(show_scalar_bar=False, show_edges=False, opacity=0.5, line_width=1,interactive=False,
                 color=True, screenshot='Image\surface_reconstruction_points.png')
'''
## 可视化点云及表面
p1 = pv.Plotter()
p1.add_mesh(surf, show_scalar_bar=False, show_edges=False, opacity=0.5,color='gray')
p1.add_mesh(clipped, opacity=0.5, scalars="cluster", categories=True)
p1.show(screenshot='Image\surface_reconstruction.png')

# 可视化GIF
p2 = pv.Plotter()
p2.add_mesh(surf, show_scalar_bar=False, show_edges=False, opacity=0.5,color='gray')
p2.add_mesh(clipped, opacity=0.5, scalars="cluster")
path = p2.generate_orbital_path(factor=2.0, shift=0, viewup=[0.5, 0.5, 1], n_points=20)
p2.open_gif('Image\surface_reconstruction.gif')
p2.orbit_on_path(path, write_frames=True, viewup=[0, 0, 1], step=1)
p2.close()
# 可视化MP4
p3 = pv.Plotter()
p3.add_mesh(surf, show_scalar_bar=False, show_edges=False, opacity=0.5,color='gray')
p3.add_mesh(clipped, opacity=0.5, scalars="cluster")
path = p3.generate_orbital_path(factor=2.0, shift=0, viewup=[0.5, 0.5, 1], n_points=20)
p3.open_movie('Image\surface_reconstruction.mp4')
p3.orbit_on_path(path, write_frames=True, viewup=[0, 0, 1], step=5)
p3.close()
'''