'''
常用正则表达式规则

1.元字符
    .       匹配除换行符以外的任意字符
    \w      匹配字母或数字或下划线或汉字
    \s      匹配任意的空白符
    \d      匹配数字
    \b      匹配单词的开始或结束
    ^       匹配字符串的开始
    $       匹配字符串的结束

2.重复
    *       重复零次或更多次
    +       重复一次或更多次
    ?       重复零次或一次
    {n}     重复n次
    {n,}    重复n次或更多次
    {n,m}   重复n到m次

3.字符类：[]
    数字：[0-9]
    大小写字母：[a-zA-Z]

4.字符串转义：\

5.条件分支：|

6.分组：()

7.贪婪与懒惰
    *?      重复任意次，但尽可能少重复
    +?      重复一次或更多次，但尽可能少重复
    ??      重复零次或一次，但尽可能少重复
    {n,m}?  重复n到m次，但尽可能少重复
    {n,}?   重复n次以上，但尽可能少重复
'''

# 实例1
