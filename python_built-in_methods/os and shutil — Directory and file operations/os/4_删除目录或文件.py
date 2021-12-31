'''

# 删除目录和文件
os.remove(path)     # 删除文件path，如果path是一个目录，抛出OSError错误，如果要删除目录请使用rmdir()
os.unlink(path)     # 同os.remove()
os.rmdir(path)      # 删除目录path，且只能删除空文件夹，否则抛出OSError错误
os.removedirs(path) # 递归删除目录,只能删除空文件夹，如果上级文件夹下有文件，则无法删除

'''