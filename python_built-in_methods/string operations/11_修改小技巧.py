'''
在Python中，字符串是不可变类型，即无法直接修改字符串的某一位字符。
Python中修改字符串的四种主要方法如下：
'''

#方法1：将字符串转换成列表后修改值，然后用join组成新字符串————最推荐！！！！
raw_str1 = 'abcdef'              #原字符串
raw_str_list1 =list(raw_str1)     #将字符串转换为列表
raw_str_list1[4]='E'             #将列表中的第5个字符修改为E
new_str1=''.join(raw_str_list1)   #用空串将列表中的所有字符重新连接为字符串
print(new_str1)

#方法2: 通过字符串序列切片方式
raw_str2='Hello World'
new_str2=raw_str2[:6] + 'Bital'
print(new_str2)

#方法3: 使用字符串的replace函数
raw_str3='abcdef'
raw_str3=raw_str3.replace('a','A')    #用A替换a
new_str3=raw_str3.replace('bcd','123')  #用123替换bcd
print(new_str3)

#方法4: 通过给一个变量赋值(或者重新赋值)
raw_str4='Hello World'
raw_str5=' 2017'       #变量赋值
new_str4=raw_str4+raw_str5
print(new_str4)