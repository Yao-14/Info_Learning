'''
re.search方法
re.search 扫描整个字符串并返回第一个成功的匹配，匹配成功re.search方法返回一个匹配的对象，否则返回None。

函数语法：re.search(pattern, string, flags=0)
    函数参数说明：
    pattern	匹配的正则表达式
    string	要匹配的字符串。
    flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
    匹配对象方法	    描述
    group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
    groups()	    返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。

re.match与re.search的区别
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
'''
import re

# re.search实例1
print(re.search('www', 'www.runoob.com').span())
print(re.search('com', 'www.runoob.com').span())

# re.search实例2 —— group使用
line = "Cats are smarter than dogs"
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")