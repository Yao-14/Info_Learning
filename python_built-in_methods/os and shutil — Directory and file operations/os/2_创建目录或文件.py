'''

# 创建目录（文件夹）和文件
os.mkdir(path)              # mkdir用于创建一个名字是path的文件夹，如果存在，则报错。
os.mkdir('test1/test2')     # 在test1文件夹下面创建一个test2文件夹，test1在创建前必须存在
os.mkdirs('test1/test2')    # 递归创建目录，即同时创建test1和test2两个文件夹，test2文件夹在test1文件夹里面，test1在创建前不存在
open(path,'w')              # open函数创建文件

'''