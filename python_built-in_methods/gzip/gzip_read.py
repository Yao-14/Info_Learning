
import io
import gzip
import pandas as pd


with gzip.open('/stDrosophila-release/stDrosophila/data/bdgp_flyfish.tsv.gz', 'rb') as input_file:
    with io.TextIOWrapper(input_file, encoding='utf-8') as dec:
        dec_list = [str(i).strip("\n").split(",") for i in dec.readlines()]
        dec_data = pd.DataFrame(dec_list[1:], columns=dec_list[0], dtype=str)
        print(dec_data)
