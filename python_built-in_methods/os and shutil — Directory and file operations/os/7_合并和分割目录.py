'''
# 合并和分割目录

# 合并目录
os.path.join(path1 [,path2[, ...]])  # 把目录和文件名合成一个路径

# 分割目录
os.path.split(path)     #将路径和文件名拆分并生成一个元组，前者为dirname，后者为filename
os.path.splitext(path)  #将路径文件名和文件名的后缀拆分并生成一个元组，前者为路径文件名，后者为后缀名

'''
import os
print(os.path.split('/BGI_college/Python built-in methods/os and shutil — Directory and file operations\\7_合并和分割目录.py'))
print(os.path.splitext(
    '/BGI_college/Python built-in methods/os and shutil — Directory and file operations\\7_合并和分割目录.py'))