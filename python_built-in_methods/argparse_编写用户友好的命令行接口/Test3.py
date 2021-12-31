'''
add_argument()方法参数须知:
    ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
        定义单个的命令行参数应当如何解析。每个形参都在下面有它自己更多的描述，包括：
     ！！   name or flags - 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
     ！！   action - 当参数在命令行中出现时使用的动作基本类型。
     ！！   nargs - 命令行参数应当消耗的数目。
            const - 被一些 action 和 nargs 选择所需求的常数。
     ！！   help - 一个此选项作用的简单描述。
            metavar - 在使用方法消息中使用的参数值示例。
     ！！   dest - 被添加到 parse_args() 所返回对象上的属性名。
            required - 此命令行选项是否可省略 （仅选项可用）。
     ！！   choices - 可用的参数的容器。
     ！！   type - 命令行参数应当被转换成的类型。
     ！！   default - 当参数未在命令行中出现并且也不存在于命名空间对象时所产生的值。
'''
import argparse
parser = argparse.ArgumentParser()
#add_argument()方法参数具体使用方法如下：

'''name or flags：add_argument() 方法必须知道它是否是一个选项，例如 -f 或 --foo，或是一个位置参数，例如一组文件名。
                  第一个传递给 add_argument() 的参数必须是一系列 flags 或者是一个简单的参数名。当 parse_args()被
                  调用，选项会以 - 前缀识别，剩下的参数则会被假定为位置参数。
                  具体例子如下：'''
#选项参数可以这么创建（-f是短参数，--foo是长参数，两者在命令行中都可以使用）：
parser.add_argument('-e1', '--example1')
#位置参数可以这么创建：
parser.add_argument('example2')

'''action：当参数在命令行中出现时使用的动作基本类型。ArgumentParser 对象将命令行参数与动作相关联。这些动作可以做与它们相关联的命令行参数的任何事，尽管大多数动作只是简单的向 parse_args() 返回的对象上添加属性。
          action 命名参数指定了这个命令行参数应当如何处理。供应的动作有：
            'store' - 存储参数的值。这是默认的动作。
            'store_const' - 存储被 const 命名参数指定的值。 'store_const' 动作通常用在选项中来指定一些标志。
            'store_true' and 'store_false' - 这些是 'store_const' 分别用作存储 True 和 False 值的特殊用例。另外，它们的默认值分别为 False 和 True。
            'append' - 存储一个列表，并且将每个参数值追加到列表中。在允许多次使用选项时很有用。
            'append_const' - 这存储一个列表，并将 const 命名参数指定的值追加到列表中。（注意 const 命名参数默认为 None。）``'append_const'`` 动作一般在多个参数需要在同一列表中存储常数时会有用。
            'count' - 计算一个关键字参数出现的数目或次数。
            请注意，default 将为 None，除非显式地设为 0。
            'help' - 打印所有当前解析器中的选项和参数的完整帮助信息，然后退出。默认情况下，一个 help 动作会被自动加入解析器。关于输出是如何创建的，参与 ArgumentParser。
            'version' - 期望有一个 version= 命名参数在 add_argument() 调用中，并打印版本信息并在调用后退出。
            'extend' - 这会存储一个列表，并将每个参数值加入到列表中。
            BooleanOptionalAction 在 argparse 中可用并会添加对布尔型操作例如 --foo 和 --no-foo 的支持。
            创建自定义动作的推荐方式是扩展 Action，重载 __call__ 方法以及可选的 __init__ 和 format_usage 方法。
'''
#store 保存参数值，可能会先将参数值转换成另一个数据类型。若没有显式指定动作，则默认为该动作。
parser.add_argument('-s', action='store', dest='simple_value',
        help='Store a simple value')
#store_const 保存一个被定义为参数规格一部分的值，而不是一个来自参数解析而来的值。这通常用于实现非布尔值的命令行标记。
parser.add_argument('-c', action='store_const', dest='constant_value',
        const='value-to-store',
        help='Store a constant value')
#store_ture/store_false 保存相应的布尔值。这两个动作被用于实现布尔开关。如下在命令行中输入-t 则会输出一个True,否则默认False。-f同理。
parser.add_argument('-t', action='store_true', default=False,
        dest='boolean_switch',
        help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=False,
        dest='boolean_switch',
        help='Set a switch to false')
#append 将值保存到一个列表中。若参数重复出现，则保存多个值。
parser.add_argument('-a', action='append', dest='collection',
        default=[],
        help='Add repeated values to a list')
#append_const 将一个定义在参数规格中的值保存到一个列表中。
parser.add_argument('-A', action='append_const', dest='const_collection',
        const='value-1-to-append',
        default=[],
        help='Add different values to list')
parser.add_argument('-B', action='append_const', dest='const_collection',
        const='value-2-to-append',
        help='Add different values to list')
#count 计算一个关键字参数出现的数目或次数。
parser.add_argument('-C', action='count', default=0)

#version 打印关于程序的版本信息，然后退出
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
'''以上Action在命令行中的结果：
 python argparse_action.py -s value
simple_value     = value
constant_value   = None
boolean_switch   = False
collection       = []
const_collection = []

$ python argparse_action.py -c
simple_value     = None
constant_value   = value-to-store
boolean_switch   = False
collection       = []
const_collection = []

$ python argparse_action.py -t
simple_value     = None
constant_value   = None
boolean_switch   = True
collection       = []
const_collection = []

$ python argparse_action.py -f
simple_value     = None
constant_value   = None
boolean_switch   = False
collection       = []
const_collection = []

$ python argparse_action.py -a one -a two -a three
simple_value     = None
constant_value   = None
boolean_switch   = False
collection       = ['one', 'two', 'three']
const_collection = []

$ python argparse_action.py -B -A
simple_value     = None
constant_value   = None
boolean_switch   = False
collection       = []
const_collection = ['value-2-to-append', 'value-1-to-append']

$ python argparse_action.py -C vvv
count = 3

$ python argparse_action.py --version
argparse_action.py 1.0

'''

'''nargs：命令行参数应当消耗的数目。对象通常关联一个单独的命令行参数到一个单独的被执行的动作。 nargs 命名参数关联不同数目的命令行参数到单一动作。支持的值有：
          N （一个整数）。命令行中的 N 个参数会被聚集到一个列表中(注意 nargs=1 会产生一个单元素列表。这和默认的元素本身是不同的)。
          '?'。如果可能的话，会从命令行中消耗一个参数，并产生一个单一项。如果当前没有命令行参数，则会产生 default 值。注意，对于选项，有另外的用例 - 选项字符串出现但没有跟随命令行参数，则会产生 const 值。一些说用用例:
          nargs='?' 的一个更普遍用法是允许可选的输入或输出文件。
          '*'。所有当前命令行参数被聚集到一个列表中。注意通过 nargs='*' 来实现多个位置参数通常没有意义，但是多个选项是可能的。
          '+'。和 '*' 类似，所有当前命令行参数被聚集到一个列表中。另外，当前没有至少一个命令行参数时会产生一个错误信息。例如:
          如果不提供 nargs 命名参数，则消耗参数的数目将被 action 决定。通常这意味着单一项目（非列表）消耗单一命令行参数。'''
#nargs=N（一个整数）,表示-n1这个参数要输入N个数据，而后生成一个列表。如-n 2 3 ，生成args.n1 = [2,3] (注意 nargs=1 会产生一个单元素列表。这和默认的元素本身是不同的)
parser.add_argument('-n1', '--nargs1', nargs=2,type=int)
#nargs='?'表示一个或0个。如果-n2不出现，则会产生 default 值；如果-n2出现但后面没有输入数据，则会产生const值
parser.add_argument('-n2', '--nargs2', nargs='?',type=int,default=10,const=20)
#nargs=”+”表示，如果你指定了-n选项，那么-n后面至少要跟一个参数，+表示至少一个

'''const：被一些 action 和 nargs 选择所需求的常数。add_argument() 的``const`` 参数用于保存不从命令行中读取但被各种 ArgumentParser 动作需求的常数值。最常用的两例为：
          当 add_argument() 通过 action='store_const' 或 action='append_const 调用时。这些动作将 const 值添加到 parse_args() 返回的对象的属性中。在 action 的描述中查看案例。
          当 add_argument() 通过选项（例如 -f 或 --foo）调用并且 nargs='?' 时。这会创建一个可以跟随零个或一个命令行参数的选项。当解析命令行时，如果选项后没有参数，则将用 const 代替。在 nargs 描述中查看案例。
          对 'store_const' 和 'append_const' 动作， const 命名参数必须给出。对其他动作，默认为 None。'''


'''help：是一个包含参数简短描述的字符串。 当用户请求帮助时（一般是通过在命令行中使用 -h 或 --help 的方式），这些help描述将随每个参数一同显示。
        具体例子如下：'''
#help一般使用方式：
parser.add_argument('-e3', '--example3', help='这是example3的帮助手册')
#help 字符串可包括各种格式描述符以避免重复使用程序名称或参数default等文本。有效的描述符包括程序名称%(prog)s和传给add_argument()的大部分关键字参数，例如 %(default)s, %(type)s 等等。
#parser.add_argument('-e4', '--example4', help='the bar to %(prog)s (default: %(default)s)')
#由于帮助字符串支持 %-formatting，如果你希望在帮助字符串中显示 % 字面值，你必须将其转义为 %%。argparse 支持静默特定选项的帮助，具体做法是将 help 的值设为 argparse.SUPPRESS:
#parser.add_argument('-e5', '--example4', help=argparse.SUPPRESS)

'''metavar：在使用方法消息中使用的参数值示例,在显示帮助信息时才会用到。当 ArgumentParser 生成帮助消息时，它需要用某种方式来引用每个预期的参数。
            默认情况下，ArgumentParser 对象使用 dest 值作为每个对象的 "name"。 默认情况下，对于位置参数动作，dest值将被直接使用。
            对于可选参数动作，dest 值将被转为大写形式。 因此，一个位置参数dest='bar' 的引用形式将为 bar，一个带有单独命令行参数的可选参数 --foo 的引用形式将为 FOO,
            而使用metavar 可以来指定一个替代名称。
            具体例子如下：'''
#metavar即参数的名字，只有在显示帮助信息时才用到。同时注意metavar仅改变显示的名称 - parse_args() 对象的属性名称仍然会由 dest 值确定。
parser.add_argument('-e6', '--example6', metavar='Ex6', help='这是example6的帮助手册')
#不同的 nargs 值可能导致 metavar 被多次使用。 提供一个元组给 metavar 即为每个参数指定不同的显示信息。
parser.add_argument('-e7', '--example7', nargs=2, metavar=('Ex7-1', 'Ex7-2'))

'''dest：被添加到 parse_args() 所返回对象上的属性名。大多数 ArgumentParser 动作会添加一些值作为 parse_args() 所返回对象的一个属性。 该属性的名称由 add_argument() 的 dest 关键字参数确定。 
         对于位置参数动作，dest 通常会作为 add_argument() 的第一个参数提供；
         对于可选参数动作，dest 的值通常取自选项字符串，ArgumentParser会通过接受第一个长选项字符串并去掉开头的 -- 字符串来生成dest的值。 ‘
         如果没有提供长选项字符串，则 dest 将通过接受第一个短选项字符串并去掉开头的 - 字符来获得。 任何内部的 - 字符都将被转换为_ 字符以确保字符串是有效的属性名称。
         而参数dest 允许提供自定义属性名称。
         
         如：parser.add_argument('-e8', '--example8', dest='try_dest')
            args = parser.parse_args()
            若要使用-e8传输的值就要使用args.try_dest
         '''
#设置dest这个选项的值就是自定义被添加到parse_args()所返回对象上的属性名
parser.add_argument('-e8', '--example8', dest='try_dest')

'''required：此命令行选项是否可省略 （仅选项可用）。 要让一个选项成为必需的，则可以将 True 作为 required= 关键字参数传给 add_argument()。
             如果一个选项被标记为 required，则当该选项未在命令行中出现时，parse_args() 将会报告一个错误。
            （必需的选项通常被认为是不适宜的，因为用户会预期 options 都是 可选的，因此在可能的情况下应当避免使用它们）
            具体例子如下：'''
#通常选项是可选的，如果需要这个选项必需有则添加required=True
parser.add_argument('-e9', '--example9', required=True)

'''choices：可用的参数的容器。某些命令行参数应当从一组受限值中选择，这可通过将一个容器对象作为 choices 关键字参数传给 add_argument() 来处理。 
            当执行命令行解析时，参数值将被检查，如果参数不是可接受的值之一就将显示错误消息。
            请注意 choices 容器包含的内容会在执行任意 type 转换之后被检查，因此 choices 容器中对象的类型应当与指定的 type 相匹配。
            任何容器都可作为 choices 值传入，因此 list 对象，set 对象以及自定义容器都是受支持的。
            不建议使用 enum.Enum，因为要控制其在用法、帮助和错误消息中的外观是很困难的。
            已格式化的选项会覆盖默认的 metavar，该值一般是派生自 dest。 这通常就是你所需要的，因为用户永远不会看到 dest 形参。 如果不想要这样的显示（或许因为有很多选择），只需指定一个显式的 metavar。
            具体例子如下：'''
#一般使用方式：-e10的输入内容只能是'rock', 'paper', 'scissors三个中的一个，不然会报错(choices可以是列表、元组，如下就是list对象）
parser.add_argument('-e10', '--example10', choices=['rock', 'paper', 'scissors'])
#choices 容器中对象的类型应当与指定的 type 相匹配，如下：
parser.add_argument('-e11', '--example11', choices=range(1,5),type=int)

'''type：命令行参数应当被转换成的类型。默认情况下，解析器会将命令行参数当作简单字符串读入，但是命令行字符串经常应当被解读为其他类型（例如 float 或 int）。 add_argument() 的 type 关键字允许执行任何必要的类型检查和类型转换。
        如果 type 关键字使用了 default 关键字，则类型转换器仅会在默认值为字符串时被应用。
        传给 type 的参数可以是任何接受单个字符串的可调用对象。 如果函数引发了 ArgumentTypeError, TypeError 或 ValueError，异常会被捕获并显示经过良好格式化的错误消息。 其他异常类型则不会被处理。
        不建议将 bool() 函数用作类型转换器。 它所做的只是将空字符串转为 False 而将非空字符串转为 True。 这通常不是用户所想要的。
        通常，type 关键字是仅应被用于只会引发上述三种被支持的异常的简单转换的便捷选项。 任何具有更复杂错误处理或资源管理的转换都应当在参数被解析后由下游代码来完成。
        例如，JSON 或 YAML 转换具有复杂的错误情况，要求给出比 type 关键字所能给出的更好的报告。 JSONDecodeError 将不会被良好地格式化而 FileNotFound 异常则完全不会被处理。
        即使 FileType 在用于 type 关键字时也存在限制。 如果一个参数使用了 FileType 并且有一个后续参数出错，则将报告一个错误但文件并不会被自动关闭。 在此情况下，更好的做法是等待直到解析器运行完毕再使用 with 语句来管理文件。
        对于简单地检查一组固定值的类型检查器，请考虑改用 choices 关键字。'''
#type：简单的解读就是使用type来确定传进来的数据是什么类型的（例如 float, int or file等可以从字符串转化过来的类型）
'''import pathlib
#普通内置类型和函数可被用作类型转换器:
parser = argparse.ArgumentParser()
parser.add_argument('count', type=int)
parser.add_argument('distance', type=float)
parser.add_argument('street', type=ascii)
parser.add_argument('code_point', type=ord)
parser.add_argument('source_file', type=open)
parser.add_argument('dest_file', type=argparse.FileType('w', encoding='latin-1'))
parser.add_argument('dest_file', type=argparse.FileType('r', encoding='latin-1'))
parser.add_argument('datapath', type=pathlib.Path)
#用户自定义的函数也可以被使用:
def hyphenated(string):
     return '-'.join([word[:4] for word in string.casefold().split()])
parser = argparse.ArgumentParser()
parser.add_argument('short_title', type=hyphenated)'''

'''default：当参数未在命令行中出现并且也不存在于命名空间对象时所产生的值。
            所有选项和一些位置参数可能在命令行中被忽略，add_argument() 的命名参数 default，默认值为 None，指定了在命令行参数未出现时应当使用的值。对于选项， default 值在选项未在命令行中出现时使用。
            提供 default=argparse.SUPPRESS 导致命令行参数未出现时没有属性被添加。
            具体例子如下：'''
#当-e12未出现在参数行时，args.12 = 42
parser.add_argument('-e12', '--example12', default=42)

args = parser.parse_args()
print(f'{args.e12}')