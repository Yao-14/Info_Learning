
'''
删除列的方法：

def data[列名]    ## def直接删除原数据中的某一列

col_data = data.pop[列名]     ## .pop删除一列的同时会产生一个返回值，返回值的内容是删除的列

new_data = data.drop(columns=[列名], inplace=False)       ### .drop()删除列/行对于原dataframe没有影响，而是生成一个新的删除了之后的dataframe (若 inplace = True 则直接在原数据上删除)

删除行的方法：

new_data = data.drop(index=[行名], inplace=False)       ### .drop()删除列/行对于原dataframe没有影响，而是生成一个新的删除了之后的dataframe (若 inplace = True 则直接在原数据上删除)

'''

