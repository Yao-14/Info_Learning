'''
dfply是一个直接在pandas中处理数据的一个拓展包，可以更方便和高效的处理dataframe数据
dfply使用方法：ddfply直接在pandas DataFrames上工作，使用>>运算符链接对数据的操作，或者以>> =从inplace操作开始。
            在dfply中，操作链的每个步骤的DataFrame结果由X表示。例如，如果要在步骤中从DataFrame中选择三列，请在
            下一步中删除第三列，然后显示最终数据的前三行，您可以执行以下操作：
            from dfply import *
            import pandas as pd
            data = pd.read_excel('example_file.xlsx',header=None)
            data.columns=['Chr','Start','End']
            df = (data >> select(X.Chr, X.Start, X.End) >> drop(X.End) >> head(3))

#注意事项1：dfply能处理的dataframe数据必须是read_excel/read_csv/read_table等输入的数据
'''
