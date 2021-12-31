'''
re.match函数
re.match 尝试从字符串的起始位置匹配一个模式，匹配成功re.match方法返回一个匹配的对象.如果不是起始位置匹配成功的话，match()就返回none。

函数语法：re.match(pattern, string, flags=0)
    函数参数说明：
    pattern	    匹配的正则表达式
    string	    要匹配的字符串。
    flags	    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志

我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
    匹配对象方法	    描述
    group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
    groups()	    返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。

'''
import re
# re.match实例1

print(re.match('www', 'www.runoob.com').span())
print(re.match('com', 'www.runoob.com'))

# re.match实例2 —— group使用
line = "Cats are smarter than dogs"
searchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")