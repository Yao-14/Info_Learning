'''
元组拆包：指将元组内的每个元素按照对应的位置，一一的赋值给不同的变量

Name，gender，age = （‘andy’， ‘man‘， 18）
_,_,age = （‘andy’， ‘man‘， 18）使用占位符，只获得age
对于所含元素较多的元组，如range（10）
a,b,*rest,c,d = range(10)获得想要的前两位和后两位，中间形成rest的一个列表

'''
#元素较少且元素全要的情况
info = ('andy', 'man', 18)
name, gender, age =('andy', 'man', 18)
print(name,gender,age,sep='   ')

#元素较少且元素不全要的情况,用占位符占据不要的元素位置
info = ('andy', 'man', 18)
_,_,age =('andy', 'man', 18)
print(age)

#元素较多且元素不全要的情况,用*rest
info = ('andy', 'man', 18, 9, 10, 66, 99, 101, 9, 79)
a,b,*rest,c = ('andy', 'man', 18, 9, 10, 66, 99, 101, 9, 79)
print(a)
print(b)
print(c)
print(rest) #rest是一个列表