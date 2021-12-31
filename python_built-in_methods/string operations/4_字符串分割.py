'''
字符串的分割方法
4.1
# string.split(str，num)         通过指定分隔符（str）对字符串进行num次切片拆分字符串，如果没有设置分隔符即默认情况下按照空格、\r、\t、 \n等空白字符进行分割。分割完成生产一个字符串的列表
# string.rsplit(str，num)        从右侧开始将字符串拆分为列表，其余同上
# string.splitlines(keepends)    装行分割符（\r、\n、\r\n）对字符串进行切片拆分字符串，返回一个包含各行作为元素的列表，如果参数keepends为False则不包含换行符，如果为True则保留换行符。

4.2
# string.partition(str)     从str出现的第一个位置起把字符串分成一个3元素的元组（分隔符前面的部分，分隔符，分隔符后面的部分组成三元素）
# string.rpartition(str)    从右侧开始将字符串拆分为列表，其余同上
'''