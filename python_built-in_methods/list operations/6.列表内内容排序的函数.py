'''
列表的排序
a)	sort：将list按特定顺序重新排列，默认由小到大，参数reverse=True可改为倒序即由大到小
    list.sort(reverse= True/False)
b)	reverse：将list倒置
    list.reverse()
'''
list00 = [99,1,72,690,57]
list00.sort() #结果为[1,57, 72, 99, 690]
print(list00)
list00.sort(reverse= True) #结果为[690, 99, 72, 57, 1]
print(list00)
list00.reverse()
print(list00) #结果再由[690, 99, 72, 57, 1]变为[1, 57, 72, 99, 690]