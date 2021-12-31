import random

x = [1,2,3,4,5,6]
print(x)
# random.shuffle()将一个列表乱序，并且是对原list做修改并保留原list
random.shuffle(x)
print(x)