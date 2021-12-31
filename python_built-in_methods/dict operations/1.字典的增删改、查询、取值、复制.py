# 新增数据
heros = {'及时雨':'宋江','玉麒麟':'卢俊义','花和尚':'鲁智深','母夜叉':'孙二娘'}
heros['豹子头'] = '林冲'
print(heros)

# 修改
heros['及时雨'] = '宋公明'
print(heros)
dict_val = {'黑旋风':'李逵','入云龙':'公孙胜','花和尚':'鲁达'}
#dict1.update(dict2)可将dict2添加在dict1的最后一个元素后，若dict2含有与dict1相同的键名则会将dict1中的值直接更新为dict2中的值
heros.update(dict_val)
print(heros)

# 删除 del , pop ,popitem , clear
heros = {'及时雨':'宋江','玉麒麟':'卢俊义','花和尚':'鲁智深','母夜叉':'孙二娘'}
# del 删除一个元素或整个字典
del heros['及时雨']
print(heros)

# pop 根据键名删除
heros.pop('花和尚')
print(heros)

# popitem 删除最后一个
heros.popitem()
print(heros)

#  clear ：将字典清空，输出为空字典
heros = {'及时雨':'宋江','玉麒麟':'卢俊义','花和尚':'鲁智深','母夜叉':'孙二娘'}
heros.clear()
print(heros)

# 查询 in
heros = {'及时雨':'宋江','玉麒麟':'卢俊义','花和尚':'鲁智深','母夜叉':'孙二娘'}
if '及时雨' in heros:
    print('该元素在字典中')
else:
    print('该元素不在字典中')

# 取值
heros = {'及时雨':'宋江','玉麒麟':'卢俊义','花和尚':'鲁智深','母夜叉':'孙二娘'}
#keys()：获得的键是获得的值是一个dict_keys([])
keys = heros.keys()
print(keys)
#list(keys)将keys的元组转变为列表
print(list(keys))
for key in keys:
    print(key)

# values()：获得的值是一个dict_values([])
values = heros.values()
print(values)
print(list(values))

# items()：获得包括键和值组成的完整元素，每个元素都是一个元组包括两个内容如('及时雨', '宋江')，
items = heros.items()
print(items)
print(list(items))
#从list（item）中分别获得键和值
key,value = list(items)[0]
print(key)
print(value)

# 复制 copy
heros_copy = heros.copy()
heros.pop('及时雨')
print(heros)
print(heros_copy)

