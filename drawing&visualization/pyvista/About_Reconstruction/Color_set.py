
import pandas as pd
import pyvista as pv
import vtk
import numpy as np
import matplotlib.pyplot as plt
# 输入点云数据 ************************************************************************************************************
data = pd.read_csv('..\Example_Data\coordinate.csv')
points = data[['x','y','z']].values
grid = pv.PolyData(points)
grid['cluster'] = data.cluster + 1
num_color = len(data.cluster.unique())

volume = grid.delaunay_3d()
surf = volume.extract_surface()
surf.subdivide(nsub=3, subfilter="loop", inplace=True)
clipped = grid.clip_surface(surf)


plot_color = ["#F56867", "#FEB915", "#C798EE", "#59BE86", "#7495D3", "#D1D1D1", "#6D1A9C", "#15821E", "#3A84E6",
                  "#997273", "#787878", "#DB4C6C", "#9E7A7A", "#554236", "#AF5F3C", "#93796C", "#F9BD3F", "#DAB370",
                  "#877F6C", "#268785"]
p = pv.Plotter()
p.add_mesh(surf, show_scalar_bar=False, show_edges=False, opacity=0.7,color='white')
p.add_mesh(clipped, opacity=0.5, scalars=clipped["cluster"], cmap=plot_color[:num_color])
p.background_color = 'black'
p.show(screenshot='Image\color_set.png',interactive=False)
