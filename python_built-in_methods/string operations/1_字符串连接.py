'''
字符串的连接方法
# string.join(seq) 以string作为分隔符，将seq中所有的元素（的字符串表示）合并为一个新的字符串
'''
list_val = ['yjj','is','handsome']
str_val = '-'.join(list_val) #通过分隔符将列表里的内容拼接在一起
print(str_val)