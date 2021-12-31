'''

                    ******** Numpy 三角函数 ********
# 三角函数
numpy.sin()         正弦函数
numpy.cos()         余弦函数
numpy.tan()         正切函数

numpy.arcsin()      反正弦函数
numpy.arccos()      反余弦函数
numpy.arctan()      反正切函数

numpy.sinh()        双曲正弦函数
numpy.cosh()        双曲余弦函数
numpy.tanh()        双曲正切函数

numpy.arcsinh()     反双曲正弦函数
numpy.arccosh()     反双曲余弦函数
numpy.arctanh()     反双曲正切函数

# 角度弧度转换函数
np.degrees()  弧度转角度:np.rad2deg()
np.radians()  角度转弧度:np.deg2rad()
'''
import numpy as np

s = np.sin(np.pi/2)  # 正弦函数
c = np.cos(np.pi/3)  # 余弦函数
t = np.tan(np.pi/4)  # 正切函数

arcs = np.arcsin(1)  # 反正弦函数
arcc = np.arccos(1)  # 反余弦函数
arct = np.arctan(1)  # 反正切函数

# 角度弧度转换函数
radian = np.pi/6
print(np.degrees(radian))  # 弧度转角度:np.rad2deg()
degrees = 45.
print(np.radians(degrees)/np.pi)  # 角度转弧度:np.deg2rad()
c1 = np.hypot(3, 4)  # 直角三角形求斜边
print(c1)
