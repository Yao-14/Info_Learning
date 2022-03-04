"""在DataFrame中复制行的方法
"""
import pandas as pd

# 方法一：通过 .append 复制行 (十分好用，但是在未来版本的pandas中可能会消失）
data1 = pd.DataFrame([["aaa", "bbb", "ccc"]])
# 你想要复制的行：data1.loc[0]
raw = data1.loc[0]
# 你想要复制的次数： 3
n_dup = 3
# 复制3行data中的第0行并添加到DataFrame中
data1 = data1.append([raw] * n_dup)
print(data1)

# 方法二：通过 pd.concat() 复制行 (也十分好用)
data2 = pd.DataFrame([["aaa", "bbb", "ccc"]])
data2 = pd.concat([data2.loc[0]] * 3, axis=1)
print(data2)


