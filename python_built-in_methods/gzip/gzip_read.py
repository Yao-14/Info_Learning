
import io
import gzip
import pandas as pd


with gzip.open('/home/yao/BGIpy37_pytorch113/Info_Learning/python_built-in_methods/gzip/deml_fbgn.tsv.gz', 'rb') as input_file:
    with io.TextIOWrapper(input_file, encoding='utf-8') as dec:
        dec_list = [str(i).strip("\n").split("\t") for i in dec.readlines()]
        dec_data = pd.DataFrame(dec_list[1:], columns=dec_list[0], dtype=str)
        print(dec_data)
