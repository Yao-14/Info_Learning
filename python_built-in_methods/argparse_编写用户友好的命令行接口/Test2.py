'''3.argparse.ArgumentParser（）方法参数须知: 一般我们只选择用description
    argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-',
                            fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True, exit_on_error=True)
        创建一个新的 ArgumentParser 对象。所有的参数都应当作为关键字参数传入。每个参数在下面都有它更详细的描述，包括：
        prog - 程序的名称（默认：sys.argv[0]）
        usage - 描述程序用途的字符串（默认值：从添加到解析器的参数生成）
        description - 在参数帮助文档之前显示的文本（默认值：无）
        epilog - 在参数帮助文档之后显示的文本（默认值：无）
        parents - 一个 ArgumentParser 对象的列表，它们的参数也应包含在内
        formatter_class - 用于自定义帮助文档输出格式的类
        prefix_chars - 可选参数的前缀字符集合（默认值：'-'）
        fromfile_prefix_chars - 当需要从文件中读取其他参数时，用于标识文件名的前缀字符集合（默认值：None）
        argument_default - 参数的全局默认值（默认值： None）
        conflict_handler - 解决冲突选项的策略（通常是不必要的）
        add_help - 为解析器添加一个 -h/--help 选项（默认值： True）
        allow_abbrev - 如果缩写是无歧义的，则允许缩写长选项 （默认值：True）
        exit_on_error - 决定当错误发生时是否让 ArgumentParser 附带错误信息退出。 (默认值: True)'''

import argparse
'''一般必要设置的几个参数：'''
#prog 默认情况下在该程序的帮助信息下这个程序的名字就是Test2.py，通过prog可以修改在该程序的帮助信息该程序的名字，如下即将程序名字修改为YJJ's first program
#usage 默认情况下在该程序的帮助信息下根据程序包含的参数来构建用法消息，即 usage：程序名字 [添加的参数1] [添加的参数2]...,通过usage可以自定义用法信息。（使用 %(prog)s 格式说明符来填入程序名称到usage中）
#description 这个参数简要描述这个程序做什么以及怎么做，在帮助消息中这个描述会显示在命令行用法字符串和各种参数的帮助消息之间。十分必要！！！！
#epilog 一些程序喜欢在 description 参数后显示额外的对程序的描述,这种文字能够通过 epilog= 参数而被指定。
#add_help 默认情况下，ArgumentParser 对象添加一个简单的显示解析器帮助信息的选项。如果不想要-h的帮助信息，则可以选择add_help = False
parser = argparse.ArgumentParser(prog="YJJ's first program",
                                 usage= ' %(prog)s [我不告诉你任何信息你能把我怎么着]',
                                 description= '这是一个什么用都没有的程序',
                                 epilog= '该程序的帮助信息就这么多！',
                                 add_help= True
                                 )
parser.add_argument('--foo', help='foo of the %(prog)s program') #通过%(prog)s即可获得prog的内容
args = parser.parse_args()
'''
exit_on_error 正常情况下，当你向 ArgumentParser 的 parse_args() 方法传入一个无效的参数列表时，它将会退出并发出错误信息。
              如果用户想要手动捕获错误，可通过将 exit_on_error 设为 False 来启用该特性:

>>> parser = argparse.ArgumentParser(exit_on_error=False)
>>> parser.add_argument('--integers', type=int)
_StoreAction(option_strings=['--integers'], dest='integers', nargs=None, const=None, default=None, type=<class 'int'>, choices=None, help=None, metavar=None)
>>> try:
...     parser.parse_args('--integers a'.split())
... except argparse.ArgumentError:
...     print('Catching an argumentError')
...
Catching an argumentError
'''


'''
#parent 有些时候，一些解析器会使用同一系列参数。 单个解析器能够通过提供 parents= 参数给 ArgumentParser 而使用相同的参数而不是重复这些参数的定义。
        parents= 参数使用 ArgumentParser 对象的列表，从它们那里收集所有的位置和可选的行为，然后将这写行为加到正在构建的 ArgumentParser 对象。

        例如：已经设定了一个解析器parent_parser，其中有参数--parent；我又设定了一个解析器foo_parser，我也想在这个解析器中设定参数--parent，我就可以用parent来获得解析器parent_parser中的参数--parent
'''
parent_parser = argparse.ArgumentParser(add_help=False) #意大多数父解析器会指定add_help=False. 否则ArgumentParse 将会看到两个-h/--help选项（一个在父参数中一个在子参数中）并且产生一个错误。
parent_parser.add_argument('--parent', type=int)
foo_parser = argparse.ArgumentParser(parents=[parent_parser])
foo_parser.add_argument('--foo')
foo_parser.parse_args()

'''
prefix_chars 许多命令行会使用 - 当作前缀，比如 -f/--foo。如果解析器需要支持不同的或者额外的字符，比如像 +f 或者 /foo 的选项，可以在参数解析构建器中使用 prefix_chars= 参数。
>>> parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
>>> parser.add_argument('+f')
>>> parser.add_argument('++bar')
>>> parser.parse_args('+f X ++bar Y'.split())
Namespace(bar='Y', f='X')
prefix_chars= 参数默认使用 '-'。 提供一组不包括 - 的字符将导致 -f/--foo 选项不被允许。'''

'''
fromfile_prefix_chars 有些时候，先举个例子，当处理一个特别长的参数列表的时候，把它存入一个文件中而不是在命令行打出来会很有意义。
                      如果 fromfile_prefix_chars= 参数提供给 ArgumentParser 构造函数，之后所有类型的字符的参数都会被当成文件处理，并且会被文件包含的参数替代。举个例子:
>>> with open('args.txt', 'w') as fp:
         fp.write('-f\nbar')
>>> parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
>>> parser.add_argument('-f')
>>> parser.parse_args(['-f', 'foo', '@args.txt'])
Namespace(f='bar')

从文件读取的参数在默认情况下必须一个一行（但是可参见 convert_arg_line_to_args()）并且它们被视为与命令行上的原始文件引用参数位于同一位置。
所以在以上例子中，['-f', 'foo', '@args.txt'] 的表示和 ['-f', 'foo', '-f', 'bar'] 的表示相同。
fromfile_prefix_chars= 参数默认为 None，意味着参数不会被当作文件对待。'''