import numpy as np
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

''' Dataframe&Series To Array '''
# method 1 : .values
print(df.values)            # Dataframe To Array
print(df['A'].values)       # Series To Array

# method 2 : np.array()
print(np.array(df))         # Dataframe To Array
print(np.array(df['A']))    # Series To Array


array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
''' Array To Dataframe '''
# method 1 : pd.DataFrame()
print(pd.DataFrame(array))

''' Array To Series '''
# method 1 : pd.Series()
print(pd.Series(array[0]))