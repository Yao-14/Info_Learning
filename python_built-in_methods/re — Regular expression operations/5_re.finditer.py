'''

re.finditer方法
re.finditer和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

函数语法：re.finditer(pattern, string, flags=0)
    函数参数说明：
    pattern	匹配的正则表达式
    string	要匹配的字符串。
    flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志
'''

import re
# re.finditer实例1
it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())