import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
plt.figure(figsize=[30,60])
sns.set_theme(style="ticks")
data = pd.DataFrame([['CHR1','AAA',2,3],['CHR2','BBB',12,13],
                     ['CHR3','CCC',21,3],['CHR1','CCC',9,6],
                     ['CHR2','AAA',10,8],['CHR3','AAA',12,3],
                     ['CHR1','BBB',2,12],['CHR2','AAA',2,8],
                     ['CHR3', 'AAA', 2, 3], ['CHR2', 'BBB', 12, 13],
                     ['CHR3', 'CCC', 1, 3], ['CHR1', 'CCC', 9, 6],
                     ['CHR1', 'AAA', 19, 8], ['CHR3', 'BBB', 12, 3],
                     ['CHR1', 'BBB', 2, 12], ['CHR2', 'AAA', 2, 8],
                     ['CHR2', 'AAA', 2, 3], ['CHR2', 'BBB', 15, 4],
                     ['CHR3', 'CCC', 21, 9], ['CHR1', 'AAA', 3, 6],
                     ['CHR2', 'CCC', 20, 8], ['CHR3', 'BBB', 1, 3],
                     ['CHR1', 'BBB', 2, 12], ['CHR2', 'CCC', 21, 1]],
                     columns=['Chr','Type','Start','End'])
strip = sns.catplot(x="Start", y="End", hue="Type", data=data,kind='strip',
                col='Chr',col_wrap=3,height=10,aspect=0.7,orient='v',
                legend=True,legend_out=True,sharex=False)
strip.savefig('strip.jpg')

swarm = sns.catplot(x="Start", y="End", hue="Type", data=data,kind='swarm',height=10,aspect=0.7,orient='v',
                legend=True,legend_out=True,sharex=False)
swarm.savefig('swarm.jpg')

box = sns.catplot(x="Start", y="End", hue="Type", data=data,kind='box',height=10,aspect=0.7,orient='v',
                legend=True,legend_out=True,sharex=False)
box.savefig('box.jpg')

violin = sns.catplot(x="Start", y="End", hue="Type", data=data,kind='violin',height=10,aspect=0.7,orient='v',
                legend=True,legend_out=True,sharex=False)
violin.savefig('violin.jpg')

boxen = sns.catplot(x="Start", y="End", hue="Type", data=data,kind='boxen',height=10,aspect=0.7,orient='v',
                legend=True,legend_out=True,sharex=False)
boxen.savefig('boxen.jpg')

point = sns.catplot(x="Start", y="End", hue="Type", data=data,kind='point',height=10,aspect=0.7,orient='v',
                legend=True,legend_out=True,sharex=False)
point.savefig('point.jpg')

bar = sns.catplot(x="Start", y="End", hue="Type", data=data,kind='bar',height=10,aspect=0.7,orient='v',
                legend=True,legend_out=True,sharex=False)
bar.savefig('bar.jpg')
