
'''
## 读取vtk文件使用pv.read()
'''

import pyvista as pv
mesh = pv.read(r'D:\BGI\A_UsefulPackages\About 3D\PyVista\Tutorial\Data\a_grid.vtk')
mesh.plot()