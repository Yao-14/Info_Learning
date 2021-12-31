'''
re.sub方法
re.sub用于查找并替换字符串中的匹配项。

函数语法：re.sub(pattern, repl, string, count=0, flags=0)
    函数参数说明：
    pattern : 正则中的模式字符串。
    repl : 替换的字符串，也可为一个函数。
    string : 要被查找替换的原始字符串。
    count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

'''
import re

# re.sub实例1
phone = "2004-959-559 # 这是一个国外电话号码"
num = re.sub(r'#.*$', "", phone)    # 删除字符串中的 Python注释
print("电话号码是: ", num)
num = re.sub(r'\D', "", phone)      # 删除非数字(-)的字符串
print("电话号码是 : ", num)

# re.sub实例2 —— repl是一个函数
def double(matched):    # 将匹配的数字乘以 2
    value = int(matched.group('value'))
    return str(value * 2)
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))