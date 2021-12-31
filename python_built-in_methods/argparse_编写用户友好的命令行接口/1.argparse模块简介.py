'''
argparse模块简介：argparse是Python内置的一个用于命令项选项与参数解析的模块，通过在程序中定义好我们需要的参数，argparse将会从sys.argv中解析出这些参数。
                 argparse 块还会自动生成帮助和使用手册，并在用户给程序传入无效参数时报出错误信息。
                当然，Python 也有第三方的库可用于命令行解析，而且功能也更加强大，比如 docopt，Click。

1. 命令行参数分为位置参数和选项参数：
    （1）位置参数就是程序根据该参数出现的位置来确定的
        如：$ ls root/ #其中root/是位置参数
    （2）选项参数是应用程序已经提前定义好的参数，不是随意指定的
        如：$ ls -l    # -l 就是ls命令里的一个选项参数

2. 使用步骤：
    （1）import argparse 首先导入模块
    （2）parser = argparse.ArgumentParser（） 创建一个解析对象
    （3）parser.add_argument() 向该对象中添加你要关注的命令行参数和选项
    （4）parser.parse_args() 解析添加的参数

3.argparse.ArgumentParser（）方法参数须知: 一般我们只选择用description
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
        exit_on_error - 决定当错误发生时是否让 ArgumentParser 附带错误信息退出。 (默认值: True)

4.add_argument()方法参数须知:
    ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
        定义单个的命令行参数应当如何解析。每个形参都在下面有它自己更多的描述，包括：
        name or flags - 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
        action - 当参数在命令行中出现时使用的动作基本类型。
        nargs - 命令行参数应当消耗的数目。
        const - 被一些 action 和 nargs 选择所需求的常数。
        default - 当参数未在命令行中出现并且也不存在于命名空间对象时所产生的值。
        type - 命令行参数应当被转换成的类型。
        choices - 可用的参数的容器。
        required - 此命令行选项是否可省略 （仅选项可用）。
        help - 一个此选项作用的简单描述。
        metavar - 在使用方法消息中使用的参数值示例。
        dest - 被添加到 parse_args() 所返回对象上的属性名。

5.parse_args()方法参数须知:
    ArgumentParser.parse_args(args=None, namespace=None)
        将参数字符串转换为对象并将其设为命名空间的属性。 返回带有成员的命名空间。之前对 add_argument() 的调用决定了哪些对象被创建以及它们如何被赋值。
        args - 要解析的字符串列表。 默认值是从 sys.argv 获取。
        namespace - 用于获取属性的对象。 默认值是一个新的空 Namespace 对象。

接下来是argparse的一些用法，分别在以下几个py文件中展示：
                    用法                    文件
            位置参数和选项参数使用简介：     Test1.py
            ArgumentParser详细使用方法：   Test2.py
            add_argument详细使用方法：     Test3.py
            实战练习1                     Test4.py
'''

