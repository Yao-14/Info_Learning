#enumerate()函数:用于获得列表内第几个元素是什么内容，
list1 = ['computer','phone','pad']
list2 = ['banana','apple','peanut']
list3 = ['tissue','desk','airpods']
list5 =[list1,list2,list3]
for i, value in enumerate(list5):
    print(i, value)
    for j, name in enumerate(value):
        print(j, name)