'''
re.compile方法
re.compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

函数语法：re.compile(pattern[, flags])
    函数参数说明：
    pattern : 一个字符串形式的正则表达式
    flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
            re.I 忽略大小写
            re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
            re.M 多行模式
            re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
            re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
            re.X 为了增加可读性，忽略空格和 # 后面的注释

当匹配成功时返回一个 Match 对象，其中：
    group([group1, …])  方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
    start([group])      方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
    end([group])        方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
    span([group])       方法返回 (start(group), end(group))。

'''

import re

# re.compile实例1
pattern = re.compile(r'\d+')                        # 用于匹配至少一个数字
print(pattern.match('one12twothree34four'))         # 查找头部，没有匹配
print(pattern.match('one12twothree34four', 2, 10))  # 从'e'的位置开始匹配，没有匹配
print(pattern.match('one12twothree34four', 3, 10))  # 从'1'的位置开始匹配，正好匹配,返回一个 Match 对象

# re.compile实例2
pattern2 = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern2.match('Hello World Wide Web')
print(m)           # 匹配成功，返回一个 Match 对象
print(m.group(0))  # 返回匹配成功的整个子串
print(m.span(0))   # 返回匹配成功的整个子串的索引
print(m.group(1))  # 返回第一个分组匹配成功的子串
print(m.span(1))   # 返回第一个分组匹配成功的子串的索引
print(m.group(2))  # 返回第二个分组匹配成功的子串
print(m.span(2))   # 返回第二个分组匹配成功的子串
print(m.groups())  # 等价于 (m.group(1), m.group(2), ...)


# re.compile实例3 —— findall
'''
findall
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
注意： match 和 search 是匹配一次 findall 匹配所有。

函数语法：findall(string[, pos[, endpos]])
    函数参数说明：
    string : 待匹配的字符串。
    pos : 可选参数，指定字符串的起始位置，默认为 0。
    endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。
'''
pattern3 = re.compile(r'\d+')  # 查找字符串中的所有数字
result1 = pattern3.findall('runoob 123 google 456')
result2 = pattern3.findall('run88oob123google456', 0, 10)
print(result1)
print(result2)