import numpy as np
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
print(df)
''' Dataframe&Series To List '''
# method 1 : .tolist()
print(df['A'].tolist())     # Series To List
print(df.values.tolist())   # Dataframe To List