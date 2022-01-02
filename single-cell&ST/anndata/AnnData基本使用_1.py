'''
AnnData的结构：
            功能	                    数据类型
adata.X	    矩阵数据	                    numpy，scipy sparse，matrix
adata.obs	观察值数据	                pandas dataframe
adata.var	特征和高可变基因数据(变量）	pandas dataframe
adata.uns	非结构化数据	                dict
'''
import numpy as np
import pandas as pd
import anndata as ad
import scanpy as sc
'''动手构建一个用于创建 AnnoData 的虚拟数据'''
# 设置观测值数量
n_obs = 10
# 生成观察时间
obs = pd.DataFrame()
obs['time'] = np.random.choice(['day 1', 'day 2', 'day 4', 'day 8'], n_obs)
# 设置特征名
var_names = [i for i in range(0, 10)]
# 特征数量
n_vars = len(var_names)
# 特征注释数据框
var = pd.DataFrame(index=var_names)
# 生成数据矩阵
X = np.arange(n_obs*n_vars).reshape(n_obs, n_vars)
#创建AnnData
adata = ad.AnnData(X, obs=obs, var=var, dtype='float64')

#在obs中添加foo列
adata.obs['foo'] = range(10)
'''查看AnnData的各个结构'''
#查看obs这个Dataframe
print('adata.obs:\n',adata.obs)
#查看obs这个Dataframe的index
print('adata.obs_names:\n',adata.obs_names)
#查看obs这个Dataframe的columns
print('adata.obs_keys:\n',adata.obs_keys())
#查看var这个Dataframe
print('adata.var:\n',adata.var)
#查看var这个Dataframe的index
print('adata.var_names:\n',adata.var_names)
#查看var这个Dataframe的columns
print('adata.var_keys:\n',adata.var_keys())
#查看X矩阵
print('adata.X:\n',adata.X)
print('adata.uns:\n',adata.uns)


'''AnnData具有切片'''
#查看obs这个Dataframe的前五列的index
print(adata.obs_names[:5].tolist())
#查看var这个Dataframe的后五列的index
print(adata.var_names[-5:].tolist())
#查看X矩阵第1、2、3列的前三个元素
print(adata[:3, [0,1,2]].X)
#在obs中添加foo列
adata.obs['foo'] = range(10)
print(adata)
'''导出数据'''
#导出为h5ad文件
adata.write("_1.h5ad")
#导出为包含csv文件的文件夹
adata.write_csvs('_1_csvs')