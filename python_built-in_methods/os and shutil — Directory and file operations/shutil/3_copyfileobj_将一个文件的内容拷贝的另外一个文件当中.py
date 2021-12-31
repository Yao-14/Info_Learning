'''
copyfileobj(fsrc, fdst, length=16*1024)： 将fsrc文件内容复制至fdst文件，length为fsrc每次读取的长度，用做缓冲区大小
            fsrc： 源文件
            fdst： 复制至fdst文件
            length： 缓冲区大小，即fsrc每次读取的长度
'''
import shutil
#将Example_file1//file111.txt中的内容复制到Example_file1//file_copy.txt中
f1 = open("1.文件夹与文件操作相关函数_主要/Example_file1/file111.txt", "r")
f2 = open("1.文件夹与文件操作相关函数_主要/Example_file1/file_copy.txt", "a+")
shutil.copyfileobj(f1,f2,length=1024)