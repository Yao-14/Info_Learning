'''
re.split方法
re.split方法按照能够匹配的子串将字符串分割后返回列表。

函数语法：re.split(pattern, string[, maxsplit=0, flags=0])
    函数参数说明：
    pattern	匹配的正则表达式
    string	要匹配的字符串。
    maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
    flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志
'''

import re
print(re.split('\W+', 'runoob, runoob, runoob.'))
print(re.split('(\W+)', ' runoob, runoob, runoob.'))
print(re.split('\W+', ' runoob, runoob, runoob.', 1))
print(re.split('a*', 'hello world'))  # 对于一个找不到匹配的字符串