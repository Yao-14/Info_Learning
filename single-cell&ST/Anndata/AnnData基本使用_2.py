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
'''读取 10X 数据'''
# 通过sc.read_10x_mtx读取10X数据， 'hg19'为mtx 文件目录；var_names指使用 gene_symbols 作为变量名；cache=True指写入缓存，可以更快的读取文件
adata = sc.read_10x_mtx('hg19', var_names='gene_symbols',cache=True)
# 索引去重，若上一步中使用 `var_names='gene_ids'` 则这一步非必须进行
adata.var_names_make_unique()
print(adata)
print(adata.var)
print(adata.obs)
print(adata.X)
# AnnData object with n_obs × n_vars = 2700 × 32738 说明数据里有2700个细胞，32738个基因