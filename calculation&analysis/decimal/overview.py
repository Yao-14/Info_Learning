'''
问题：浮点数一个普遍的问题就是在计算机的世界中，浮点数并不能准确地表示十进制。并且，即便是最简单的数学运算，也会带来不可控制的后果。因为，在计算机的世界中只认识0与1。因此在有些需要精确表示浮点数的场合，例如财务结算，这些误差就不可接受。

decimal 模块：decimal解决了浮点数的运算精度问题，提升了运算精度的同时，肯定带来的是性能的损失。在对数据要求特别精确的场合（例如财务结算），这些性能的损失是值得的。但是如果是大规模的科学计算，就需要考虑运行效率了。毕竟原生的float比Decimal对象肯定是要快很多的。
使用decimal模块的注意事项：可以传递给Decimal整型或者字符串参数，但不能是浮点数据，因为浮点数据本身就不准确。
'''

from decimal import Decimal, getcontext

#1.输入数据的方法
#1.1对于整型或者字符串,要将整型或者字符串数据转换为Decimal类型————Decimal(8)
print(Decimal(8))
print(Decimal('5.5'))
#1.2浮点数也可以str(22.222)转换成字符串再进行————Decimal(str(22.222))
print(Decimal(str(22.222)))

#2.输出结果样式的设置
#2.1通过设定有效数字，限定结果样式————getcontext().prec = 4
getcontext().prec = 4 #设定结果保留4位有效数字
result1 = Decimal(str(22.222)) + Decimal(str(22.222))
print(type(result1))
#2.2通过设定保留多少位小数，限定结果样式————result2.quantize(Decimal('0.000'))
result2 = Decimal(1) / Decimal(3)
print(result2.quantize(Decimal('0.000'))) #设定结果保留3位小数
#2.3四舍五入取整的几种形式————result3.quantize(Decimal('0.000'),rounding='ROUND_CEILING')
     #ROUND_CEILING 总是趋向无穷大向上取整
     #ROUND_DOWN　总是趋向0取整
     #ROUND_FLOOR 总是趋向负无穷大向下取整
     #ROUND_HALF_DOWN　如果最后一个有效数字大于或等于5则朝0反方向取整；否则，趋向0取整
     #ROUND_HALF_EVEN　类似于ROUND_HALF_DOWN，不过，如果最后一个有效数字值为5，则会检查前一位。偶数值会导致结果向下取整，奇数值导致结果向上取整
     #ROUND_HALF_UP 类似于ROUND_HALF_DOWN，不过如果最后一位有效数字为5，值会朝0的反方向取整
     #ROUND_UP　朝0的反方向取整
     #ROUND_05UP　如果最后一位是0或5，则朝0的反方向取整；否则向0取整
result3 = Decimal(1) / Decimal(3)
print(result3.quantize(Decimal('0.000'),rounding='ROUND_CEILING')) #设定结果保留3位小数,且向上取整，结果位0.334

#3.由于得到的数据结果是Decimal类型，因而需要将Decimal 结果转化为string或浮点数或整数————str(result4)、float(result4)、int(result4)
result4 = Decimal(1) / Decimal(3)
print(type(float(result4)),float(result4))
print(type(str(result4)),str(result4))
