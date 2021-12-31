'''
1.字体大小：fontsize = 20
2.字体粗细：weight = 'bold'————粗细程度可选：'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy','extra bold','black'
3.字体风格：styles = 'normal'————一般字体风格有'normal'、'italic'、'oblique'
4.字体颜色：color = 'red'
5.字体方向：rotation = 30
6.字体格式：family = 'Arial'————一般英文字体会用'Times New Roman'和'Arial'
        若要使用中文字体，则需要将字体格式设置为以下任意一种，使用字体格式的英文名。如family = 'SimHei'
                黑体： SimHei
                微软雅黑： Microsoft YaHei
                微软正黑体： Microsoft JhengHei
                新宋体 ： NSimSun
                新细明体 ： PMingLiU
                细明体 ： MingLiU
                标楷体 ： DFKai-SB
                仿宋 ： FangSong
                楷体 ： KaiTi
                仿宋_GB2312： FangSong_GB2312
                楷体_GB2312： KaiTi_GB2312
                隶书：LiSu
                幼圆：YouYuan
                华文细黑：STXihei
                华文楷体：STKaiti
                华文宋体：STSong
                华文中宋：STZhongsong
                华文仿宋：STFangsong
                方正舒体：FZShuTi
                方正姚体：FZYaoti
                华文彩云：STCaiyun
                华文琥珀：STHupo
                华文隶书：STLiti
                华文行楷：STXingkai
                华文新魏：STXinwei
7.统一字体可以用一个字典来控制，如下：
    font = {'family': 'serif',
            'style': 'italic',
            'weight': 'normal',
            'color': 'darkred',
            'size': 16,
            'rotation' :30}
    而后在需要设置字体的地方输入fontdict=font即可。如plt.text(fontdict=font)
'''
