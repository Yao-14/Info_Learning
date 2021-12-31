'''
move(src, dst)： 将src移动至dst目录下。若dst目录不存在，则效果等同于src改名为dst。若dst目录存在，将会把src文件夹的所有内容移动至该目录下面
            src：源文件夹或文件
            dst：移动至dst文件夹，或将文件改名为dst文件。如果src为文件夹，而dst为文件将会报错
            copy_function：拷贝文件的方式，可以传入一个可执行的处理函数。默认为copy2，Python3新增参数
'''

import shutil
#将Example_file3文件夹移动至Example_file2文件夹下面，如果Example_file2文件夹不存在，则变成了重命名操作
shutil.move('Example_file3', '1.文件夹与文件操作相关函数_主要/Example_file2')
# 将Example_file1文件夹中的file2.txt移动至Example_file2文件夹下面，如果Example_file2文件夹不存在，则变成了重命名操作
shutil.move('Example_file1//file2.txt', '1.文件夹与文件操作相关函数_主要/Example_file2')
# 将Example_file1文件夹中的file1.txt重命名为file111.txt文件(file111.txt文件存在，将会覆盖)
shutil.move('Example_file1//file1.txt', '1.文件夹与文件操作相关函数_主要/Example_file1/file111.txt')
