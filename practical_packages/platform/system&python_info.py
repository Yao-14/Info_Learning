#python platform

import platform

def show_os_all_info():
    '''打印os的全部信息'''
    print(f'获取操作系统名称及版本号 : {platform.platform()}')
    print(f'获取操作系统版本号 : {platform.version()}')
    print(f'获取操作系统的位数 : {platform.architecture()}')
    print(f'计算机类型 : {platform.machine()}')
    print(f'计算机的网络名称 : {platform.node()}')
    print(f'计算机处理器信息 : {platform.processor()}')
    print(f'获取操作系统类型 : {platform.system()}')
    print(f'汇总信息 : {platform.uname()}')

def show_python_all_info():
    '''打印python的全部信息'''
    print(f'The Python build number and date as strings : {platform.python_build()}')
    print(f'The compiler used for compiling Python : {platform.python_compiler()}')
    print(f'The Python implementation SCM branch : {platform.python_branch()}')
    print(f'The Python implementation : {platform.python_implementation()}')
    print(f'The version of Python ： {platform.python_revision()}')
    print(f'Python implementation SCM revision : {platform.python_version()}')
    print(f'Python version as tuple : {platform.python_version_tuple()}')

if __name__ == '__main__':
    print('操作系统信息:')
    show_os_all_info()
    print('#' * 100)
    print('计算机中的python信息：')
    show_python_all_info()