
import io
import gzip
import pandas as pd

with open("/home/yao/BGIpy37_pytorch113/ST_Drosophila/1_Preprocessing/LassoByUbiquitousGenes/filter_flymine.csv", "r") as f:
    content = f.readlines()
    print(content)

with gzip.open('/home/yao/BGIpy37_pytorch113/ST_Drosophila/stDrosophila/data/bdgp_flyfish.tsv.gz', 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.writelines(content)

