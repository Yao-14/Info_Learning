'''
匿名函数lambda：是指一类无需定义标识符（函数名）的函数或子程序。
lambda 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值。

语法： lambda [arg1 [,arg2,.....argn]]:expression
        冒号前是参数，可以有多个，用逗号隔开，冒号右边的为表达式（只能为一个）。其实lambda返回值是一个函数的地址，也就是函数对象。
'''

#1.可以将lambda函数替代一些简单的函数，如下两者的意义相同
def sum1(x,y):
    return x+y
print(sum1(1,2))

sum2 = lambda x,y : x+y
print(sum2(1,2))

#2.lambda函数可以作为参数传递给其他函数。部分Python内置函数接收函数作为参数
def odd(x):
    return x%2
show1 = list(filter(odd,range(10)))
print(show1)   #[1, 3, 5, 7, 9]
show2 = list(filter(lambda x: x%2,range(10)))
print(show2)

#3.将if...else语句缩减为单一的条件表达式————语法为：expression1 if A else expression2 如果A为True，条件表达式的结果为expression1，否则为expression2
def s1(x):
    if x==1:
        return "yes"
    else:
        return "no"
s2=lambda x:"yes" if x==1 else "no"
print(s2(0))

