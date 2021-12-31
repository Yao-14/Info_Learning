'''
字符串的is判断方法
8.1
# string.isdigit()       如果string只包含数字则返回True，否则返回False
# string.isalpha()       如果string至少有一个字符并且所有字符都是字母则返回True，否则返回False
# string.isalnum()       如果string至少有一个字符并且所有字符都是字母或数字则返回True，否则返回False
# string.isdecimal()     如果string只包含十进制数字则返回True，否则返回False
# string.isnumeric()     如果string中只包含数字字符则返回True，否则返回False

8.2
# string.islower()       如果string中包含至少一个区分大小写的字符，并且所有这些区分大小写的字符都是小写，则返回True，否则返回False
# string.isupper()       如果string中包含至少一个区分大小写的字符，并且所有这些区分大小写的字符都是大写，则返回True，否则返回False
# string.istitle()       如果string是标题化的，则返回True，否则返回False（标题化即string.title(),见字符串大小写转换）

8.3
# string.isspace()       如果string中只包含空格，则返回True，否则返回False
# string.isprintable()   判断所有字符是否都可打印。如果字符串中的所有字符都是可打印的或字符串为空（不可打印的字符可以是回车和换行符），则返回True。如果不是，则返回False。
# string.isidentifier()  判断字符串是否是有效的 Python 标识符（即判断目标字符串是否只含数字、字母、下划线），可用来判断变量名是否合法。如果字符串是有效的 Python 标识符返回 True，否则返回 False

'''


string = '1T2wq4 ;['
# isdigit       如果string只包含数字则返回True，否则返回False
print(string.isdigit())
# isalpha       如果string至少有一个字符并且所有字符都是字母则返回True，否则返回False
print(string.isalpha())
# isalnum       如果string至少有一个字符并且所有字符都是字母或数字则返回True，否则返回False
print(string.isalnum())
# isdecimal     如果string只包含十进制数字则返回True，否则返回False
print(string.isdecimal())
# isnumeric     如果string中只包含数字字符则返回True，否则返回False
print(string.isnumeric())
# islower       如果string中包含至少一个区分大小写的字符，并且所有这些区分大小写的字符都是小写，则返回True，否则返回False
print(string.islower())
# isupper       如果string中包含至少一个区分大小写的字符，并且所有这些区分大小写的字符都是大写，则返回True，否则返回False
# istitle       如果string是标题化的，则返回True，否则返回False
print(string.istitle())
# isspace       如果string中只包含空格，则返回True，否则返回False
print(string.isspace())
# isprintable   判断所有字符是否都可打印。如果字符串中的所有字符都是可打印的或字符串为空（不可打印的字符可以是回车和换行符），则返回True。如果不是，则返回False。
print(string.isprintable())
# isidentifier  判断字符串是否是有效的 Python 标识符（即判断目标字符串是否只含数字、字母、下划线），可用来判断变量名是否合法。如果字符串是有效的 Python 标识符返回 True，否则返回 False
print(string.isidentifier())

