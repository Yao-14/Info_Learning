
'''
读取大数据使用分块读取
'''

import pandas as pd

def readViaChunk(path, sep='\t', chunksize=5000):
    data = pd.read_csv(path, sep=sep, engine='python', iterator=True, chunksize=chunksize)
    chunks = []
    loop = True
    while loop:
        try:
            chunk = data.get_chunk()
            chunks.append(chunk)
        except StopIteration:
            loop = False

    allData = pd.concat(chunks)
    return allData

data = readViaChunk(path='..\_Example_data.txt')
print(data)