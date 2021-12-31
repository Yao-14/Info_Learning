'''
# 遍历子目录
os.listdir(path)                             # 返回path指定的文件夹包含的文件或文件夹的名字的列表
os.walk(top,topdown=True,onerror=None,followlinks=False)     # 输出在文件夹中的文件名通过在树中游走，向上或者向下

# 详细补充
os.walk(top,topdown=True,onerror=None,followlinks=False)     # 输出在文件夹中的文件名通过在树中游走，向上或者向下
    top         所要遍历的目录的path，返回的是一个三元组(root,dirs,files)
                    # root 所指的是当前正在遍历的这个文件夹的本身的地址
                    # dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
                    # files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
    topdown     可选，为True则优先遍历top目录，否则优先遍历top的子目录
    onerror     可选，需要一个callable对象，当walk需要异常时会调用
    followlinks 可选，为True则会遍历目录下的快捷方式实际所指的目录，如果为False则优先遍历top的子目录
'''
import os
path = os.getcwd()
for root, dirs, files in os.walk(path):
    #遍历所有文件夹，获得所有文件夹的路径
    listdirs = [os.path.join(root,dirname) for dirname in dirs]
    # 遍历所有文件，获得所有文件的路径
    listfiles = [os.path.join(root, filename) for filename in files]

# os.listdir(path)：输出该文件夹下的所有文件和文件夹（只是子文件和子文件夹，子文件夹中的内容不输出）
dirs = os.listdir(path)
for file in dirs:
    print(file)
