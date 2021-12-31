import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_theme(style="ticks")

data = pd.DataFrame([['gene1','day1','sp1',20],['gene1','day1','sp2',23],['gene1','day1','sp3',21],['gene1','day1','sp4',29],
                     ['gene1','day2','sp1',27],['gene1','day2','sp1',12],['gene1','day2','sp3',16],['gene1','day2','sp4',22],
                     ['gene1','day3','sp1',31],['gene1','day3','sp2',32],['gene1','day3','sp3',28],['gene1','day3','sp4',26],
                     ['gene2','day1','sp1',20],['gene2','day1','sp2',23],['gene2','day1','sp3',21],['gene2','day1','sp4',29],
                     ['gene2','day2','sp1',27],['gene2','day2','sp1',12],['gene2','day2','sp3',16],['gene2','day2','sp4',22],
                     ['gene2','day3','sp1',31],['gene2','day3','sp2',32],['gene2','day3','sp3',28],['gene2','day3','sp4',26],
                     ['gene3','day1','sp1',20],['gene3','day1','sp2',23],['gene3','day1','sp3',21],['gene3','day1','sp4',29],
                     ['gene3','day2','sp1',27],['gene3','day2','sp1',12],['gene3','day2','sp3',16],['gene3','day2','sp4',22],
                     ['gene3','day3','sp1',31],['gene3','day3','sp2',32],['gene3','day3','sp3',28],['gene3','day3','sp4',26]],
                     columns=['Gene','Day','Species','Expression'])
test1 = sns.boxplot(x="Gene", y="Expression", hue="Species", data=data,palette='Set1',orient='v',order=['gene1','gene2'])
plt.savefig('Example1.pdf')