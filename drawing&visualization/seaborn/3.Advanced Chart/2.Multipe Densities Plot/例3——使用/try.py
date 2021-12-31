import pandas as pd

data = pd.read_csv('N032N03-all-results.txt',header=None,sep=' ')
data.columns= ['Seq','Ka','Ks','Ka/Ks','4dtv_corrected']
dataneed = data.loc[:,('Seq','Ks')]
dataneed.to_csv('N03_N03_Ks.txt',sep='\t',header=False,index=False)