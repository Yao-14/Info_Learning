'''
map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
语法： map(function, iterable, ...)
'''
def square(x) :         # 计算平方数
    return x ** 2
map(square, [1,2,3,4,5])    # 计算列表各个元素的平方
list(map(square, [1,2,3,4,5]))   # 使用 list() 转换为列表
list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
