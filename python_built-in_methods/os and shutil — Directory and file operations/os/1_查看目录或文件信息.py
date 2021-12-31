'''
# 查看目录或文件信息
os.getcwd()                # 查看当前文件所在的目录
os.path.realpath(path)     # 获取path的真实路径
os.path.abspath(path)      # 获取path的绝对路径
os.path.getsize(path)      # 获取文件的大小，如果文件不存在则返回错误
os.path.getctime(path)     # 获取文件的创建时间
os.path.getatime(path)     # 获取文件的最近访问时间
os.path.getmtime(path)     # 获取文件的最近修改时间
os.stat(path)              # 获取指定路径的信息，返回信息如下
                                st_mode     inode保护模式
                                st_ino      inode节点号
                                st_dev      inode驻留的设备
                                st_nlink    inode的链接数
                                st_uid      所有者的用户ID
                                st_gid      所有者的组ID
                                st_size     普通文件以字节为单位的大小；包含等待某些特殊文件的数据
                                st_atime    上次访问的时间
                                st_mtime    最后一次修改的时间
                                st_ctime    由操作系统报告的“ctime”。在windows平台上是创建时间，在Unix上是最新的元数据更改的时间
'''
import os
print(os.getcwd()) # 查看当前文件所在的目录
print(os.stat(''))
print(os.path.abspath(''))
print(os.path.realpath(''))
