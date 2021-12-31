'''
copytree(src, dst, symlinks=False, ignore=None)： 拷贝文档树，将src文件夹里的所有内容拷贝至dst文件夹
         !!!src：源文件夹
         !!!dst：复制至dst文件夹，该文件夹会自动创建，需保证此文件夹不存在，否则将报错
            symlinks：是否复制软连接，True复制软连接，False不复制，软连接会被当成文件复制过来，默认False
         !!!ignore：忽略模式，可传入ignore_patterns()
            copy_function：拷贝文件的方式，可以传入一个可执行的处理函数，默认为copy2，Python3新增参数
            ignore_dangling_symlinks：sysmlinks设置为False时，拷贝指向文件已删除的软连接时，将会报错，如果想消除这个异常，可以设置此值为True。默认为False,Python3新增参数
'''
import shutil
#将Example_file1文件夹复制至Example_file3文件夹。Example_file3文件夹会自动创建，需保证此文件夹不存在，否则将报错。
shutil.copytree('1.文件夹与文件操作相关函数_主要/Example_file1', 'Example_file3')
#将Example_file2文件夹复制至Example_file4文件夹，同时将Example_file2文件夹中的"file1.txt","file4.txt"两个文件忽略，不复制
shutil.copytree('1.文件夹与文件操作相关函数_主要/Example_file2', 'Example_file4', ignore=shutil.ignore_patterns("file1.txt", "file4.txt"))