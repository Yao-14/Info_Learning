'''
列表的删除：
a)	del：根据索引进行删除
b)	pop：删除最后一个元素
c)	remove：根据元素的值进行删除（若存在多个相同元素，只删除最前面的一个）
'''
list12 = ['banana', 'pineapple', 'apple', 'peanut']
del list12[-2] #删除apple
print(list12)
list12.pop()    #删除peanut
print(list12)
list12.remove('banana') #删除banana
print(list12)