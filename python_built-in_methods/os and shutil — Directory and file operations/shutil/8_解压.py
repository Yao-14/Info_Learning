'''
unpack_archive(filename, extract_dir=None, format=None)： 解压操作。Python3新增方法
            filename：文件路径
            extract_dir：解压至的文件夹路径。文件夹可以不存在，会自动生成
            format：解压格式，默认为None，会根据扩展名自动选择解压格式
'''
import shutil
zip_path = '2.归档操作相关函数_主要/压缩后文件夹.zip'
extract_dir = '2.归档操作相关函数_主要/解压后文件夹'
shutil.unpack_archive('2.归档操作相关函数_主要/压缩后文件夹.zip', '解压后文件夹')