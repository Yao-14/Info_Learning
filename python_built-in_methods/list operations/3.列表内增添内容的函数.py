'''
列表增添内容的函数
list.append（元素）：向列表最后面添加元素
list.insert（位置，元素）：在指定位置index前插入元素
list.extend（另一个列表）：可以将另一个集合中的元素逐一添加到列表最后
'''
listk = ['computer','phone','pad']
listm = ['banana','apple','peanut']
listk.append('jjjj') #得到['computer', 'phone', 'pad', 'jjjj']
listm.insert(1,'lll') #得到['banana', 'lll', 'apple', 'peanut']
listk.extend(listm) #得到['computer', 'phone', 'pad', 'jjjj', 'banana', 'lll', 'apple', 'peanut']
