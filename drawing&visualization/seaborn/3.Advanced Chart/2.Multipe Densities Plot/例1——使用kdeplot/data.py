import pandas as pd

data = pd.read_csv('JniJni.txt',sep = '\t')
data['Seq'] = 'Juni_Juni'
data2 = pd.read_csv('JsiJsi.txt',sep = '\t',header=None)
data2[0] = 'Jsi_Jsi'
data2.columns =['Seq','Ks']
data3 = pd.concat([data2,data],axis=0,ignore_index=True)
print(data3)
data3.to_csv('data.txt',header=False,index=False,sep='\t')