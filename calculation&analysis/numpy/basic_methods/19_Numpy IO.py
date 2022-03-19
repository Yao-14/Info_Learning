'''

                    ******** Numpy IO 简介 ********

NumPy IO
Numpy 可以读写磁盘上的文本数据或二进制数据。
NumPy 为 ndarray 对象引入了一个简单的文件格式：npy。
npy 文件用于存储重建 ndarray 所需的数据、图形、dtype 和其他信息。

                    ******** Numpy 常用的 IO 函数 ********

load() 和 save() 函数是读写文件数组数据的两个主要函数，默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为 .npy 的文件中。
savez() 函数用于将多个数组写入文件，默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为 .npz 的文件中。
loadtxt() 和 savetxt() 函数处理正常的文本文件(.txt 等)

                    ******** Numpy 常用的 IO 函数详情 ********

numpy.save(file, arr, allow_pickle=True, fix_imports=True) 函数将数组保存到以 .npy 为扩展名的文件中。
        file：要保存的文件，扩展名为 .npy，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上。
        arr: 要保存的数组
        allow_pickle: 可选，布尔值，允许使用 Python pickles 保存对象数组，Python 中的 pickle 用于在保存到磁盘文件或从磁盘文件读取之前，对对象进行序列化和反序列化。
        fix_imports: 可选，为了方便 Pyhton2 中读取 Python3 保存的数据。

numpy.savez(file, *args, **kwds) 函数将多个数组保存到以 npz 为扩展名的文件中。
        file：要保存的文件，扩展名为 .npz，如果文件路径末尾没有扩展名 .npz，该扩展名会被自动加上。
        args: 要保存的数组，可以使用关键字参数为数组起一个名字，非关键字参数传递的数组会自动起名为 arr_0, arr_1, …　。
        kwds: 要保存的数组使用关键字名称。


numpy.savetxt(FILENAME, a, fmt="%d", delimiter=",") 函数是以简单的文本文件格式存储数据
        delimiter: 可以指定各种分隔符、针对特定列的转换器函数、需要跳过的行数等。
numpy.loadtxt(FILENAME, dtype=int, delimiter=' ')  函数是读取以简单的文本文件格式存储数据
        delimiter: 可以指定各种分隔符、针对特定列的转换器函数、需要跳过的行数等。

'''