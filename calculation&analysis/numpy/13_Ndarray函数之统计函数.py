'''

                    ******** Numpy 统计函数 ********

numpy.amin(a, axis)    计算数组中的元素沿指定轴的最小值。
numpy.amax(a, axis)    计算数组中的元素沿指定轴的最大值。
numpy.ptp(a, axis)     计算数组中元素最大值与最小值的差（最大值 - 最小值）。
numpy.median(a, axis)  计算数组中元素的中位数
numpy.mean(a, axis)    计算数组中元素的算术平均值。
numpy.average(a, axis, returned) 根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值。(不指定权重时相当于 mean 函数）（如果 returned 参数设为 true，则返回权重的和）
numpy.std(a, axis)     计算数组中元素的标准差。
numpy.var(a, axis)     计算数组中元素的方差。
numpy.percentile(a, q, axis)    百分位数是统计中使用的度量，表示小于这个值的观察值的百分比（q: 要计算的百分位数，在 0 ~ 100 之间）

主要参数：
a: 输入数组
axis: 沿着它计算百分位数的轴（None,0,1)

百分位数：第 p 个百分位数是这样一个值，它使得至少有 p% 的数据项小于或等于这个值，且至少有 (100-p)% 的数据项大于或等于这个值。
加权平均值：即将各数值乘以相应的权数，然后加总求和得到总体值，再除以总的单位数。
标准差：标准差是一组数据平均值分散程度的一种度量，标准差是方差的算术平方根。
方差：统计中的方差（样本方差）是每个样本值与全体样本值的平均数之差的平方值的平均数，即 mean((x - x.mean())** 2)。
'''
import numpy as np
a = np.array([[10, 7, 4], [3, 2, 1]])
# numpy.amin(a, axis)    计算数组中的元素沿指定轴的最小值。
print('调用 amin() 函数,axis=None：\n',np.amin(a,axis=None)) # 将数组展开为一维数组后计算
print('调用 amin() 函数,axis=1：\n',np.amin(a,axis=1))       # 沿轴 1 计算
print('调用 amin() 函数,axis=0：\n',np.amin(a,axis=0))       # 沿轴 0 计算

# numpy.amax(a, axis)    计算数组中的元素沿指定轴的最大值。
print('调用 amax() 函数,axis=None：\n',np.amax(a,axis=None)) # 将数组展开为一维数组后计算
print('调用 amax() 函数,axis=1：\n',np.amax(a,axis=1))       # 沿轴 1 计算
print('调用 amax() 函数,axis=0：\n',np.amax(a,axis=0))       # 沿轴 0 计算

# numpy.ptp(a, axis)     计算数组中元素最大值与最小值的差（最大值 - 最小值）。
print ('调用 ptp() 函数,axis=None：\n',np.ptp(a))            # 将数组展开为一维数组后计算
print ('调用 ptp() 函数,axis=1：\n',np.ptp(a, axis =  1))    # 沿轴 1 计算
print ('调用 ptp() 函数,axis=0：\n',np.ptp(a, axis =  0))    # 沿轴 0 计算

# numpy.median(a, axis)  计算数组中元素的中位数
print ('调用 median() 函数,axis=None：\n',np.median(a))            # 将数组展开为一维数组后计算
print ('调用 median() 函数,axis=1：\n',np.median(a, axis =  1))    # 沿轴 1 计算
print ('调用 median() 函数,axis=0：\n',np.median(a, axis =  0))    # 沿轴 0 计算

# numpy.mean(a, axis)    计算数组中元素的算术平均值。
print ('调用 mean() 函数,axis=None：\n',np.mean(a))            # 将数组展开为一维数组后计算
print ('调用 mean() 函数,axis=1：\n',np.mean(a, axis =  1))    # 沿轴 1 计算
print ('调用 mean() 函数,axis=0：\n',np.mean(a, axis =  0))    # 沿轴 0 计算

# numpy.average(a, axis, returned) 根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值。(不指定权重时相当于 mean 函数）（如果 returned 参数设为 true，则返回权重的和）
wts = np.array([[3, 2, 2], [1, 1, 0]])
print ('调用 average() 函数,axis=None：\n',np.average(a,weights=wts))            # 将数组展开为一维数组后计算
print ('调用 average() 函数,axis=1：\n',np.average(a, weights=wts, axis =  1))    # 沿轴 1 计算
print ('调用 average() 函数,axis=0：\n',np.average(a, weights=wts, axis =  0))    # 沿轴 0 计算

# numpy.std(a, axis)     计算数组中元素的标准差。
print ('调用 std() 函数,axis=None：\n',np.std(a))            # 将数组展开为一维数组后计算
print ('调用 std() 函数,axis=1：\n',np.std(a, axis =  1))    # 沿轴 1 计算
print ('调用 std() 函数,axis=0：\n',np.std(a, axis =  0))    # 沿轴 0 计算

# numpy.var(a, axis)     计算数组中元素的方差。
print ('调用 var() 函数,axis=None：\n',np.var(a))            # 将数组展开为一维数组后计算
print ('调用 var() 函数,axis=1：\n',np.var(a, axis =  1))    # 沿轴 1 计算
print ('调用 var() 函数,axis=0：\n',np.var(a, axis =  0))    # 沿轴 0 计算

# numpy.percentile(a, q, axis)    百分位数是统计中使用的度量，表示小于这个值的观察值的百分比（q: 要计算的百分位数，在 0 ~ 100 之间）
print ('调用 percentile() 函数,axis=None：\n',np.percentile(a,q= 50 ,))            # 将数组展开为一维数组后计算
print ('调用 percentile() 函数,axis=1：\n',np.percentile(a,q= 50 , axis =  1))    # 沿轴 1 计算
print ('调用 percentile() 函数,axis=0：\n',np.percentile(a,q= 50 , axis =  0))    # 沿轴 0 计算


