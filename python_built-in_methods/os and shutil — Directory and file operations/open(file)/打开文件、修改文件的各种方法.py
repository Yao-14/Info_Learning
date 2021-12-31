#r:对打开的文件只读，不能修改
#file1 = open('利用tbtools.txt', 'r')
#w：对打开的文件只能修改，不能读取，并且文件的修改是将原内容清空后在添加新的内容
#file2 = open('利用tbtools.txt', 'w')
#a：对打开的文件只能修改，并且文件的修改不会将原内容清空，而是在原内容后面添加新的内容
#file3 = open('利用tbtools.txt', 'a')
#r+：对打开的文件即可读又可写，但是文件的修改是从原内容的开头开始覆盖原内容
#file4 = open('利用tbtools.txt', 'r+')
#w+：对打开的文件即可读又可写，同时文件的修改是将原内容清空后在添加新的内容
#file5 = open('利用tbtools.txt', 'w+')
#a+：对打开的文件即可读又可写，但是文件的修改是在原内容后面开始添加新的内容
#file5 = open('利用tbtools.txt', 'a+')

#文件指针：file.seek（offset[,whence])：offset表示要把文件指针先移动到哪个位置上；whence有0、1、2三个选项，0表示从当前文件指针移动到的位置上开始算起
file = open('2.txt', 'w+')
file.write('sssjjshss')
file.seek(4,0)
content = file.read()
print(content)
file.close()
#结果是jshss

#写入文件内容的方法write和writelines
file1 = open('3.txt','w')
content1 = file1.write("我是姚佳俊")
#若输入的内容在文件中需要换行，则用换行符\n，如下
content2 = file1.write('woshiyjj,\n我是姚佳俊')
#若输入的内容是一个字符串列表/元组等，则用writelines
list = ['\njj','kk','ll','aa']
content3 = file1.writelines(list)
#若输入的内容在文件中需要换行，则用\n，如下
#join函数用于在每个字符串之间添加一个内容
content4 = file1.writelines('\n'.join(list))
file1.close()

#读取文件内容的方法read、readline和readlines
#read：读取全部内容，返回一个字符串
#readline：读取当前文件指针所在一行内容，返回一个字符串，并且会自动换行
#readlines：每次读取一行内容，最终返回一个字符串列表
file2 = open('4.txt','r+')
file2.write('第一行\n第二行\n第三行\n第四行\n第五行')
content2 = file2.readlines()
#由于文本内容分为多行，每一行的结尾都会默认含有换行符，因此生成的列表的每一项字符串后面都有换行符\n，为了去掉\n如下
list = []
for i in content2:
    g = i.strip('\n')
    list.append(g)
print(list)
file2.close()

#每次文件用完之后都需要file.close（）关闭文件
#若使用with语句则不需要自己关闭文件，python会自动关闭，如下：
with open('4.txt','r') as file3:
    content3 = file3.readlines()
    print(content3)


