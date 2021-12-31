from dfply import *
import pandas as pd
a = pd.DataFrame({
        'x1':['A','B','C'],
        'x2':[1,2,3]})
b = pd.DataFrame({
    'x1':['A','B','D'],
    'x3':[True,False,True]})

#1.inner_join():
print(a >> inner_join(b, by='x1'))
#结果是：  x1  x2     x3
#      0  A   1   True
#      1  B   2  False

#2.outer_join()/full_join():
print(a >> outer_join(b, by='x1'))
#结果是：  x1   x2     x3
#      0  A  1.0   True
#      1  B  2.0  False
#      2  C  3.0    NaN
#      3  D  NaN   True

#3.left_join():
print(a >> left_join(b, by='x1'))
#结果是：  x1  x2     x3
#      0  A   1   True
#      1  B   2  False
#      2  C   3    NaN
#4.right_join():
print(a >> right_join(b, by='x1'))
#结果是：  x1   x2     x3
#      0  A  1.0   True
#      1  B  2.0  False
#      2  D  NaN   True

#5.semi_join():
print(a >> semi_join(b, by='x1'))
#结果是： x1  x2
#     0  A   1
#     1  B   2

#6.anti_join():
print(a >> anti_join(b, by='x1'))
#结果是：   x1  x2
#       2  C   3