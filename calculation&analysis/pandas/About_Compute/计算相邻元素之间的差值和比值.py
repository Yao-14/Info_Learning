
'''对于Dataframe，按照行或列计算相邻元素的之间的差值或比值'''

import pandas as pd
df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6],
                  'b': [1, 1, 2, 3, 5, 8],
                  'c': [1, 4, 9, 16, 25, 36]})


# 计算元素之间的差值 DataFrame.diff(periods=1, axis=0)
    # periods：默认值是1，计算当前元素和前一个元素的差值(若为-1则计算当前元素与后一个元素的差值，若为2则计算当期元素与前两个元素的差值，以此类推）
    # axis：axis=0，表示按照row进行平移，axis=1，表示按照列进行平移
print(df.diff(periods=1))
print(df.diff(periods=2))


# 计算元素之间的比值 DataFrame.pct_change(periods=1, fill_method='pad', limit=None, freq=None, **kwargs)
    # periods：平移的距离，默认值是1
    # fill_method：如何处理NA，默认值是pad
    # limit：填充的最大NA的数量，如果NA的数量大于limit，那么停止填充NA元素
print(df.pct_change())