'''

        ******** numpy.frombuffer ********

numpy.frombuffer (buffer, dtype=float, count=-1, offset=0)  将data以流的形式读入转化为一维数组ndarray对象。

        buffer: buffer_like. 公开缓冲区接口的对象。
        dtype:  data-type, optional. 返回数组的数据类型； 默认值为 float。
        count:  int, optional. 代表返回的ndarray的长度。默认值为 -1，表示缓冲区中的所有数据。
        offset: int, optional. 偏移量，代表读取的起始位置(以字节表示)；默认值为 0。

如果buffer具有非机器字节顺序的数据，则应将其指定为数据类型的一部分。

IDX文件格式文件简介：IDX文件包括idx1、idx3等格式，IDX后面的数字表示数据维度，也就是一般图像文件为3维，标签文件为1维。

'''
import numpy as np
import gzip

# 1维标签文件
idx1_path = 'Example data/t10k-labels-idx1-ubyte.gz'
with gzip.open(idx1_path, 'rb') as lbpath:
    buffer1 = lbpath.read()
    print(buffer1)
    idx1array = np.frombuffer(buffer1, np.uint8, offset=8)
    print(idx1array)

# 3维图像文件
idx3_path = 'Example data/t10k-images-idx3-ubyte.gz'
with gzip.open(idx3_path, 'rb') as imgpath:
    buffer3 = imgpath.read()
    print(buffer3)
    idx3array = np.frombuffer(buffer3, np.uint8, offset=16).reshape(len(idx1array), 28, 28)
    print(idx3array)