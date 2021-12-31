'''
seaborn.clustermap可能会用到的参数
data2D:array-like
用于聚类的矩形数据。不能包含NA。

method:str, optional
用于计算聚类的链接方法。有关更多信息，请参见scipy.cluster.hierarchy.linkage（）文档。
    method=’single’
        for all points  in cluster  and  in cluster . This is also known as the Nearest Point Algorithm.
    method=’complete’
        for all points  in cluster u and  in cluster . This is also known by the Farthest Point Algorithm or Voor Hees Algorithm.
    method=’average’
        for all points  and  where  and  are the cardinalities of clusters  and , respectively. This is also called the UPGMA algorithm.
    method=’weighted’
        where cluster u was formed with cluster s and t and v is a remaining cluster in the forest (also called WPGMA).
    method=’centroid’
        where  and  are the centroids of clusters  and , respectively. When two clusters  and  are combined into a new cluster , the new centroid is computed over all the original objects in clusters  and . The distance then becomes the Euclidean distance between the centroid of  and the centroid of a remaining cluster  in the forest. This is also known as the UPGMC algorithm.
    method=’median’
        like the centroid method. When two clusters  and  are combined into a new cluster , the average of centroids s and t give the new centroid . This is also known as the WPGMC algorithm.
    method=’ward’
        uses the Ward variance minimization algorithm. The new entry  is computed as follows,
        where  is the newly joined cluster consisting of clusters  and ,  is an unused cluster in the forest, , and  is the cardinality of its argument. This is also known as the incremental algorithm.


metric:str, optional
用于数据的距离度量。有关更多选项，请参见scipy.spatial.distance.pdist（）文档。要对行和列使用不同的度量标准（或方法），您可以自己构造每个链接矩阵，并将其提供为{row，col} _linkage。
    The distance metric to use. The distance function can be ‘braycurtis’, ‘canberra’, ‘chebyshev’, ‘cityblock’, ‘correlation’,
                                                             ’cosine’, ‘dice’, ‘euclidean’, ‘hamming’, ‘jaccard’, ‘jensenshannon’,
                                                             ‘kulsinski’, ‘mahalanobis’, ‘matching’, ‘minkowski’, ‘rogerstanimoto’,
                                                             ‘russellrao’, ‘seuclidean’, ‘sokalmichener’, ‘sokalsneath’, ‘sqeuclidean’, ‘yule’.

z_score:int or None, optional
0（行）或1（列）。是否计算行或列的z分数。 Z分数是：z =（x-平均值）/ std，因此每一行（列）中的值将减去该行（列）的平均值，然后除以该行的标准差（列）。这样可确保每一行（列）的均值为0，方差为1。

standard_scale:int or None, optional
0（行）或1（列）。是否要标准化该尺寸（对于每一行或每一列而言），请减去最小值，然后将其除以最大值。

figsize：tuple of (width, height), optional
图的整体大小。

cbar_kws:dict, optional
关键字参数传递给heatmap（）中的cbar_kws，例如在颜色栏上添加标签。

{row,col}_cluster:bool, optional
如果为True，则将{行，列}聚类。

{row,col}_linkage:numpy.ndarray, optional
行或列的预先计算的链接矩阵。有关特定格式，请参见scipy.cluster.hierarchy.linkage（）。

{row,col}_colors:list-like or pandas DataFrame/Series, optional
要为行或列标记的颜色列表。有助于评估组内的样本是否聚集在一起。可以将嵌套列表或DataFrame用于多个颜色级别的标签。如果以pandas.DataFrame或pandas.Series的形式给出，则从DataFrames列名称或系列名称中提取颜色的标签。 DataFrame / Series颜色还通过其索引与数据匹配，以确保以正确的顺序绘制颜色。

mask:bool array or DataFrame, optional
如果通过，数据将不会显示在mask为True的单元格中。缺少值的单元格将被自动屏蔽。仅用于可视化，不用于计算。

{dendrogram,colors}_ratio:float, or pair of floats, optional
图形大小的比例专用于两个边际元素。如果给出一对，则它们对应于（行，列）比率。

cbar_postuple of (left, bottom, width, height), optional
彩条轴在图中的位置。设置为“无”将禁用颜色栏。

tree_kws:dict, optional
matplotlib.collections.LineCollection的参数，用于绘制树状图的线条。
'''




