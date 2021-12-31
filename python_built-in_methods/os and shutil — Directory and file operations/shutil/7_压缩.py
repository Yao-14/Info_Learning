'''
make_archive(base_name, format, root_dir, …)： 生成压缩文件
            base_name：压缩文件的文件名，不允许有扩展名，因为会根据压缩格式生成相应的扩展名
            format：压缩格式
            root_dir：将制定文件夹进行压缩

get_archive_formats()： 获取支持的压缩文件格式。目前支持的有：tar、zip、gztar、bztar。在Python3还多支持一种格式xztar
'''

import shutil
base_name = '压缩后文件夹'
format = "zip"
root_dir = '2.归档操作相关函数_主要/Example_file1'
# 将会root_dir文件夹下的内容进行压缩，生成一个压缩后文件夹.zip文件
shutil.make_archive(base_name, format, root_dir)