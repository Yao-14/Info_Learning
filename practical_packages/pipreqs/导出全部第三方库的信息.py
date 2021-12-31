import sys
import os
# 找到当前目录
project_root = os.path.dirname(os.path.realpath(__file__))
print(project_root)

# 找到解释器，虚拟环境目录
python_root = sys.exec_prefix
print(python_root)

# 1、导出全部第三方库的信息
# 拼接生成requirement命令
command = python_root + '\Scripts\pip freeze > ' + project_root + '\\requirements1.txt'
os.system(command)
