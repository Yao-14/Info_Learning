
'''
## 读取jpg, png等图像使用pv.read()
'''

import pyvista as pv
image = pv.read('D:\BGI\A_UsefulPackages\About 3D\PyVista\Tutorial\Data\Gourds2.jpg')
image.plot(rgb=True, cpos="xy")
