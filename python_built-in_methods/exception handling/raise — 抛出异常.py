'''

Python 使用 raise 语句抛出一个指定的异常。

************ raise 语句完整格式 ************
raise [Exception [, args [, traceback]]]

'''

# Example1：以下实例如果 x 大于 5 就触发异常。
x = 3
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

# Example2：raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
#          如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

# 用户自定义异常：你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承，例如:

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message