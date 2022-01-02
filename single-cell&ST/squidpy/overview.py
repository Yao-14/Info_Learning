'''
import squidpy as sq


Graph
gr.spatial_neighbors(adata[, spatial_key, …])       从空间坐标创建图形。
gr.nhood_enrichment(adata, cluster_key[, …])        通过置换测试计算邻域丰富度。
gr.co_occurrence(adata, cluster_key[, …])           计算集群的共现概率。
gr.centrality_scores(adata, cluster_key[, …])       计算每个集群或细胞类型的中心性分数。
gr.interaction_matrix(adata, cluster_key[, …])      计算集群的交互矩阵。
gr.ripley(adata, cluster_key[, mode, …])            计算点过程的各种 Ripley 统计量。
gr.ligrec(adata, cluster_key[, …])                  按照 [Efremova et al., 2020] 中的描述执行置换测试。
gr.spatial_autocorr(adata[, …])                     计算全局自相关统计量（Moran's I 或 Geary's C）。
gr.sepal(adata, max_neighs[, genes, n_iter, …])     用萼片识别空间可变基因。


Image
im.process(img[, layer, library_id, method, …])     通过应用变换来处理图像。
im.segment(img[, layer, library_id, method, …])     分割图像。
im.calculate_image_features(adata, img[, …])        计算 .adata 中所有观察的图像特征。


Plotting
pl.nhood_enrichment(adata, cluster_key[, …])        邻里富集分析绘制邻里富集图
pl.centrality_scores(adata, cluster_key[, …])       绘制中心性分数。
pl.interaction_matrix(adata, cluster_key[, …])      绘制集群交互矩阵。
pl.ligrec(adata[, cluster_key, …])                  绘制受体-配体置换测试的结果。
pl.ripley(adata, cluster_key[, mode, …])            为每个集群绘制 Ripley 的统计数据。
pl.co_occurrence(adata, cluster_key[, …])           绘制每个集群的共现概率比。
pl.extract(adata[, obsm_key, prefix])               创建一个临时的 anndata.AnnData 对象用于绘图。


Datasets
datasets.four_i([path])                             来自 Gut 等人的预处理子集 4i 数据集。
datasets.imc([path])                                Jackson 等人的预处理子集 IMC 数据集。
datasets.seqfish([path])                            Lohoff 等人的预处理子集 seqFISH 数据集。
datasets.merfish([path])                            来自 Moffitt 等人的预处理 MERFISH 数据集。
datasets.mibitof([path])                            来自 Hartmann 等人的预处理 MIBI-TOF 数据集。
datasets.slideseqv2([path])                         来自 Stickles 等人的预处理 SlideseqV2 数据集。
datasets.sc_mouse_cortex([path])                    预处理的 scRNA-seq 小鼠皮层。
datasets.visium_hne_adata([path])                   预处理的 10x Genomics Visium H&E 数据集。
datasets.visium_hne_adata_crop([path])              预处理子集 10x Genomics Visium H&E 数据集。
datasets.visium_fluo_adata([path])                  预处理的 10x Genomics Visium 荧光数据集。
datasets.visium_fluo_adata_crop([path])             预处理子集 10x Genomics Visium 荧光数据集。
datasets.visium_hne_image([path])                   来自 10x Genomics Visium 数据集的 H&E 图像。
datasets.visium_hne_image_crop([path])              来自 10x Genomics Visium 数据集的裁剪 H&E 图像。
datasets.visium_fluo_image_crop([path])             来自 10x Genomics Visium 数据集的裁剪荧光图像。
'''