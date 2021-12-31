import argparse
parser = argparse.ArgumentParser()
#位置参数是必须输入的值，选项参数是不一定要输入的值
#位置参数使用例子：在使用Test1.py时必须先输入x的值，再输入y的值。
parser.add_argument("x", help="请输入矩形的长",type=int)
parser.add_argument("y", help="请输入矩形的宽",type=int)
#选项参数使用例子：在使用Test1.py时输入--name后再输入name的值
parser.add_argument("--name", help="请输入矩形的名字",type=str,default='YJJ')
args = parser.parse_args()
print(f'{args.name}矩形的面积是{args.x * args.y}')