import argparse
import pandas as pd
parser = argparse.ArgumentParser(prog="Modify GFF file",
                                 usage= ' %(prog)s',
                                 description= '通过Modify GFF file可以将原始的GFF文件修改为简洁的只包含Chr, Gene ID, Start, End的文件',
                                 epilog= '该程序的帮助信息就这么多！十分简单！',
                                 add_help= True)

parser.add_argument("-i","--input",dest='input_file',type=str,help='请输入GFF文件名')
parser.add_argument("-o","--output",dest='output_file', type=str, help="请输入输出文件名")
args = parser.parse_args()

data = pd.read_csv(args.input_file,header=None,sep='\t')
data1 = data[data[2].map(lambda e:e == 'gene')]
data2 = data1.loc[:,[0,3,4,8]]
data2.columns = ['Chr', 'Start', 'End', 'ID']
data2.index = range(len(data2.index))
data2['ID'] = data2['ID'].map(lambda e: e[3:17])
data2['Chr'] = data2['Chr'].map(lambda e: f'Jre_Chr0{e[-1]}' if len(e) == 4 else f'Jre_Chr{e[-2:]}')
data2.to_csv(f'{args.output_file}', index=False, header=False, sep='\t')
