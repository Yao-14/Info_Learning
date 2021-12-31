'''
#调色盘的颜色风格有：
    Pastel1,Pastel2,Paired,Accent,Dark2,Set1,Set2,Set3,tab10,tab20,tab20b,tab20c
    Greys,Purples,Blues,Greens,Oranges,Reds,YlOrBr,YlOrRd,OrRd,PuRd,RdRu,BuRu,GnBu,PuBu,YlGnBu,PuBuGn,BuGn,YlGn
    binary,gist_yarg,gist_gray,gray,bone,pink,spring,summer,autumn,winter,cool,Wistia,hot,afmhot,gist_heat,copper
    PiYG,PRGn,BrBG,PuOr,RdGy,RdBu,RdYlBu,RdYlGn,Spectral,coolwarm,bwr,seismic
    viridis,plasma,inferno,magma,cividis
    twiligjt,twiligjt_shifted,hsv

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!风格颜色转换：在颜色代码后加上_r（如Blues/Blues_r）!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
import matplotlib.pyplot as plt
import seaborn as sns
sns.palplot(sns.color_palette(palette='rainbow',n_colors =10,as_cmap =False))

'''
n_colors：从调色盘中挑选的颜色色块个数（如n_colors =8指选择8个颜色色块）
palette：调色盘的颜色风格（如palette='Accent'指选择Accent这个颜色风格）
as_cmap：默认为False，返回颜色列表。如果为True值，则返回matplotlib colormap而不是颜色列表。
'''
plt.show()
