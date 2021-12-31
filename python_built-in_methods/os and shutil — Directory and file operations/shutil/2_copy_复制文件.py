'''
copy(src, dst)： 将文件src复制至dst。dst可以是个目录，会在该目录下创建与src同名的文件，若该目录下存在同名文件，将会报错提示已经存在同名文件。权限会被一并复制。本质是先后调用了copyfile与copymode而已
            src：源文件路径
            dst：复制至dst文件夹或文件
            follow_symlinks：设置为False时，src, dst皆为软连接，可以复制软连接权限，如果设置为True，则当成普通文件复制权限。默认为True。Python3新增参数
'''

import shutil
#将Example_file1文件夹下的file1文件复制到Example_file2文件夹中
shutil.copy("Example_file1//file1.txt", "1.文件夹与文件操作相关函数_主要/Example_file2")
#将Example_file1文件夹下的file1文件复制到Example_file2文件夹中,并且重新命名为file5.txt
shutil.copy("Example_file1//file1.txt", "1.文件夹与文件操作相关函数_主要/Example_file2/file5.txt")