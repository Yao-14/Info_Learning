'''

                    ******** Numpy 字符串函数 ********

以下函数用于对 dtype 为 numpy.string_ 或 numpy.unicode_ 的数组执行向量化字符串操作。 它们基于 Python 内置库中的标准字符串函数。
                  函数	                            描述
            numpy.char.add()	        对两个数组的逐个字符串元素进行连接
            numpy.char.multiply()	    返回按元素多重连接后的字符串
            numpy.char.center()	        居中字符串
            numpy.char.capitalize()	    将字符串第一个字母转换为大写
            numpy.char.title()	        将字符串的每个单词的第一个字母转换为大写
            numpy.char.lower()	        数组元素转换为小写
            numpy.char.upper()	        数组元素转换为大写
            numpy.char.split()	        指定分隔符对字符串进行分割，并返回数组列表
            numpy.char.splitlines()	    返回元素中的行列表，以换行符分割
            numpy.char.strip()	        移除元素开头或者结尾处的特定字符
            numpy.char.join()	        通过指定分隔符来连接数组中的元素
            numpy.char.replace()	    使用新字符串替换字符串中的所有子字符串
            numpy.char.decode()	        函数对编码的元素进行 str.decode() 编码。默认编码是 utf-8，可以使用标准 Python 库中的编解码器
            numpy.char.encode()	        函数对编码的元素进行 str.decode() 解码。

'''
import numpy as np
# numpy.char.add()	            对两个数组的逐个字符串元素进行连接
print (np.char.add(['hello'],[' xyz']))
print (np.char.add(['hello', 'hi'],[' abc', ' xyz']))

# numpy.char.multiply()	        返回按元素多重连接后的字符串
print (np.char.multiply('Runoob ',3))

# np.char.center(str , width,fillchar) 居中字符串    # str: 字符串，width: 长度，fillchar: 填充字符
print (np.char.center('Runoob', 20,fillchar = '*'))

# numpy.char.capitalize()	    将字符串第一个字母转换为大写
print (np.char.capitalize('runoob'))

# numpy.char.title()	        将字符串的每个单词的第一个字母转换为大写
print (np.char.title('i like runoob'))

# numpy.char.lower()	        数组元素转换为小写
print (np.char.lower(['RUNOOB','GOOGLE']))
print (np.char.lower('runoob'))

# numpy.char.upper()	        数组元素转换为大写
print (np.char.upper(['runoob','google']))
print (np.char.upper('runoob'))

# numpy.char.split()	        指定分隔符对字符串进行分割，并返回数组列表(默认sep= 空格）
print (np.char.split ('www.runoob.com', sep = '.'))

# numpy.char.splitlines()	    返回元素中的行列表，以换行符分割
print (np.char.splitlines('i\rlike runoob?'))

# numpy.char.strip()	        移除元素开头或者结尾处的特定字符
print (np.char.strip(['arunooba','admin','java'],'a'))

# numpy.char.join()	            通过指定分隔符来连接数组中的元素
print (np.char.join(':','runoob'))
print (np.char.join([':','-'],['runoob','google']))

# numpy.char.replace()	        使用新字符串替换字符串中的所有子字符串
print (np.char.replace ('i like runoob', 'oo', 'cc'))

# numpy.char.decode()	        函数对编码的元素进行 str.decode() 编码。默认编码是 utf-8，可以使用标准 Python 库中的编解码器
# numpy.char.encode()	        函数对编码的元素进行 str.decode() 解码。
a = np.char.encode('runoob', 'cp500')
print(a)
print (np.char.decode(a,'cp500'))

