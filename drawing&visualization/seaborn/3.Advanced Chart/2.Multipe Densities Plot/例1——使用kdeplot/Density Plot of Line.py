'''
绘制多重密度曲线图，需要输入的txt文件类似于下面格式即可：
Species	            Ks
SpeciesA_SpeciesA	5.549548562
SpeciesA_SpeciesA	5.136655092
SpeciesA_SpeciesA	5.001806241
SpeciesA_SpeciesA	4.973012539
SpeciesA_SpeciesA	4.923420372
SpeciesA_SpeciesA	4.868327119
SpeciesA_SpeciesA	4.746737276
SpeciesA_SpeciesE	2.82528
SpeciesA_SpeciesE	2.9308
SpeciesA_SpeciesE	1.33376
SpeciesA_SpeciesE	1.67648
SpeciesA_SpeciesE	1.99569
SpeciesA_SpeciesE	3.15274
SpeciesA_SpeciesE	2.75167
SpeciesA_SpeciesE	1.71715
SpeciesA_SpeciesE	2.68106
SpeciesA_SpeciesF	0.0502102
SpeciesA_SpeciesF	0.0520385
SpeciesA_SpeciesF	0.0313209
SpeciesA_SpeciesF	0.0491324
SpeciesA_SpeciesF	0.027394
SpeciesA_SpeciesF	0.103598
SpeciesA_SpeciesF	0.28731
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Create the data
def create_data(file):
    print('开始提取数据>>')
    data = pd.read_csv(file,sep = '\t')
    dropdata = data[data['Ks'].map(lambda e: e < 10 and e != None)]
    dropdata.index = range(0,len(dropdata.index))
    print(dropdata)
    print('结束提取数据>>')
    return dropdata

def label(Ks, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontsize = 25,fontweight="bold", color=color,
            ha="right", va="center", transform=ax.transAxes)

def Draw_the_densities(data,savefile,xlabel,colorall):
    print('开始绘图>>')
    data.columns = ['Species', xlabel]
    new_columns = [i for i in data.columns]
    sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
    pal = sns.color_palette(colorall)
    Species = sns.FacetGrid(data, row="Species", hue="Species", aspect=15, height=2, palette=pal)
    # Draw the densities in a few steps
    Species.map(sns.kdeplot, new_columns[1],
          bw_adjust=1.5, clip_on=False,
          fill=True, alpha=1, linewidth=1.5)
    Species.map(sns.kdeplot, new_columns[1], clip_on=False, color="w", lw=2, bw_adjust=1.5)
    Species.map(plt.axhline, y=0, lw=2, clip_on=False)
    Species.map(plt.grid,axis="x", linewidth = 3,color = 'gainsboro')
    Species.map(label,new_columns[1])
    # Set the subplots to overlap
    Species.fig.subplots_adjust(hspace=-.25)
    # Remove axes details that don't play well with overlap
    Species.set_titles("")
    Species.set_xlabels(fontsize= 25,weight="bold")
    Species.set(yticks=[])
    Species.despine(bottom=True, left=True)
    Species.savefig(savefile)

if __name__ == '__main__':
    file = 'Ks.txt'
    xlabel = 'Synonymous substitution rate (Ks)'
    colorall = 'Paired'
    savefile = 'chart1.pdf'
    data = create_data(file)
    Draw_the_densities(data, savefile,xlabel,colorall)