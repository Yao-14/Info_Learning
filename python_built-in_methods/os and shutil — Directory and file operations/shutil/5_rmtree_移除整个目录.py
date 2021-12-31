'''
rmtree(path, ignore_errors=False, οnerrοr=None)： 移除文档树，将文件夹目录删除
            path:需要删除的文件夹路径
            ignore_errors：是否忽略错误，默认False
            onerror：定义错误处理函数，需传递一个可执行的处理函数，该处理函数接收三个参数：函数、路径和excinfo
'''
import shutil
#将Example_file4文件夹目录删除
shutil.rmtree('Example_file4')