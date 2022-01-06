
import io
import gzip
import pandas as pd

with open("deml_fbgn.csv", "r") as f:
    content = f.readlines()
    print(content)

with gzip.open('/home/yao/BGIpy37_pytorch113/Info_Learning/python_built-in_methods/gzip/deml_fbgn.tsv.gz', 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.writelines(content)

