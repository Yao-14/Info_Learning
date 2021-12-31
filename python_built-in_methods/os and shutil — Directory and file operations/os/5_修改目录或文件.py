'''

# 修改目录和文件
os.rename(src,dst)        # 重命名文件或目录，从src到dst
os.chdir(path)            # 改变当前工作目录
os.access(path,mode)      # 用当前的uid/gid尝试访问路径
os.chmod(path,mode)       # 更改权限
os.chown(path,uid,gid)    # 更改文件所有者

# 详细补充
os.access(path,mode)      # 用当前的uid/gid尝试访问路径，如果允许访问返回True，否则返回False
    path 要用来检测是否有访问权限的路径
    mode mode为F_OK，测试存在的路径，或者它可以是包含R_OK、W_OK和X_OK或者R_OK、W_OK和X_OK其中之一或者更多
        os.F_OK 作为access()的mode参数，测试path是否存在
        os.R_OK 包含在access()的mode参数中，测试path是否可读
        os.W_OK 包含在access()的mode参数中，测试path是否可写
        os.X_OK 包含在access()的mode参数中，测试path是否可执行

os.chmod(path,mode)       # 更改权限，更改权限会删除之前所有的权限，进行重新的更改
    path 文件名路径或目录路径
    mode 可用以下选项按位或操作生成。文件权限以用户id->组id->其他顺序检验，最先匹配的允许或者禁止权限被应用。
         stat.S_IXOTH   其他用户有执行权0o001
         stat.S_IWOTH   其他用户有写权限0o002
         stat.S_IROTH   其他用户有读权限0o004
         stat.S_IRWXO   其他用户有全部权限（权限掩码）0o007
         stat.S_IXGRP   组用户有执行权0o010
         stat.S_IWGRP   组用户有写权限0o020
         stat.S_IRGRP   组用户有读权限0o040
         stat.S_IRWXG   组用户有全部权限（权限掩码）0o070
         stat.S_IXUSR   拥有者具有执行权0o100
         stat.S_IWUSR   拥有者具有写权限0o200
         stat.S_IRUSR   拥有者具有读权限0o400
         stat.S_IRWXU   拥有者具有全部权限（权限掩码）0o700
         stat.S_ISVTX   目录里文件目录只有拥有者才可删除更改0o1000
         stat.S_ISGID   执行此文件其进程有效组为文件所在组0o2000
         stat.S_ISUID   执行此文件其进程有效用户为文件所有者0o4000
         stat.S_IREAD   windows下设为只读
         stat.S_IWRITE  windows下取消只读
         增加多个权限使用+号进行连接

    示例： 增加单个权限 —— os.chmod(path,stat.S_IREAD)
          增加多个权限 —— os.chmod(path,stat.S_IREAD+stat.S_IWOTH)
'''