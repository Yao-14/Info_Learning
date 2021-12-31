'''

异常：即便 Python 程序的语法是正确的，在运行它的时候，也有可能发生错误。此时运行期检测到的错误被称为异常。
     大多数的异常都不会被程序处理，都以错误信息的形式以不同的类型出现，异常类型包括 ZeroDivisionError, NameError, TypeError等。

************ try 语句完整格式 ************
        try:
            子句1
        except (异常类型1,异常类型2,异常类型3):
            子句2
        else:
            子句3
        finally:
            子句4

'''

'''
try 语句按照如下方式工作1；
    try:
        子句1
    except 异常类型:
        子句2
# 注意事项1：一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，即 except (异常类型1, 异常类型2, 异常类型3):
# 注意事项2：如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。

'''
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except: # 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。
    print("Unexpected error:", sys.exc_info()[0])
    raise

'''

try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。
else 子句将在 try 子句没有发生任何异常的时候执行。

try 语句按照如下方式工作2；
    try:
        子句1
    except 异常类型:
        子句2
    else:
        子句3

'''
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

'''

finally 子句无论是否发生异常都将执行最后的代码。

try 语句按照如下方式工作3；
    try:
        子句1
    except 异常类型:
        子句2
    else:
        子句3
    finally:
        子句4
'''
try:
    runoob()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')