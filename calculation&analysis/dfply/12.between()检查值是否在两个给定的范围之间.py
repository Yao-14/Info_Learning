from dfply import *
import pandas as pd
data = pd.read_excel('example_file.xlsx',header=None)
data.columns=['Chr','Start','End']
#between(X.Size, 100, 500)：检测X.Size的值是否在100到500之间，是的话返回True，不是的话返回False
df1 = data >> mutate(Size=X.End-X.Start) >> mutate(size_btwn=between(X.Size, 100, 500)) >> head(5)
print(df1)