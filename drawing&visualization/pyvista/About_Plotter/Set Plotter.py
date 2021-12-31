'''

************ 创建 pv.Plotter 对象 ************
plotter = pv.Plotter(off_screen=True,             ## 是否关闭弹出交互窗口(在集群、流程中等使用时建议True)
                     shape=(1,1),                 ## 绘制子图个数，指定方法有如下三种：
                                                     shape=(2,2) 指定一个二乘二的网格绘制 4 个子图
                                                     shape="3|1" 表示左侧有 3 个图，右侧有 1 个图 (个人认为最好)
                                                     shape="4/2" 表示顶部有 4 个图，底部有 2 个图
                     window_size=[1024, 768]      ## 生成图像的大小
                     border=True,                 ## 是否在每个子图周围绘制边框
                     border_color='white',        ## 边框颜色
                     multi_samples=8,             ## 用于减少混叠的多个样本数(4是一个很好的默认值；但8会有更好的结果，对性能有潜在的影响)
                     line_smoothing=False,        ## 是否启用线条平滑
                     polygon_smoothing=False,     ## 是否启用多边形平滑
                     lighting='light_kit',        ## 设置照明强度('light_kit'(五灯), 'three lights'(三灯), 'none'(无灯))
                     )

************ 向 pv.Plotter 对象添加 mesh (此方法使用网格表示来查看数据集的表面和/或几何形状，以下是主要参数) ************
plotter.add_mesh(mesh,                  ## 支持任何 PyVista 或 VTK 网格。
                 color=None,            ## 设置用于整个网格的单一纯色。(如果要设置不同颜色则保持color=None)
                 style='surface',       ## 设置网格的可视化样式。(包括style='surface', style='wireframe', style='points')
                 scalars=None,          ## 设置用于“着色”网格的标量。接受存在于网格上的数组的字符串名称或与网格中的单元数或点数相等的数组。
                 clim=None,             ## 设置标量的颜色条范围，默认为标量数组的最小值和最大值。示例：[-1, 2]。
                 show_edges=None,       ## 是否显示网格的边缘。(不适用于style='wireframe')
                 edge_color=None,       ## 设置当 show_edges=True 时边缘颜色。
                 point_size=5.0,        ## 设置任何节点的点大小。
                 line_width=None,       ## 线条粗细。仅对style='wireframe' 和 style='surface' 有效。
                 opacity=1.0,           ## 网格的不透明度。(介于0-1之间)
                 flip_scalars=False,    ## 翻转 cmap 的方向。
                 cmap=None,             ## 指定颜色列表
                 show_scalar_bar=None,  ## 如果为 False，则不会将标量条添加到场景中。
                 nan_color=None,        ## 设置数组中所有 NaN 值的颜色。
                 nan_opacity=1.0,       ## 设置数组中所有 NaN 值的不透明度。(介于0-1之间)
                 silhouette=False,      ## 如果设置为 True，则为网格绘制轮廓高光。此功能仅适用于 PolyData。
                 below_color=None,      ## 设置标量范围(clim)以下值的纯色。
                 above_color=None,      ## 设置标量范围(clim)以上值的颜色。
                 log_scale=False,       ## 将数据映射到颜色时使用对数刻度。
                 )

************ 向 pv.Plotter 对象添加 volume (此方法使用网格表示来查看数据集的表面和/或几何形状) ************
plotter.add_volume()

************ 设置相机位置 ('xy', 'xz', 'yz', 'yx', 'zx', 'zy', 'iso') ************
plotter.camera_position = 'iso'

************ 添加文本 ************
plotter.add_text(text,
                 position='upper_left', ## 设置放置文本框的位置，包括'lower_left','lower_right','upper_left','upper_right',
                                                                'lower_edge','upper_edge','right_edge','left_edge'.
                 font_size=18,          ## 设置文本字体的大小。
                 color=None,            ## 设置文本字体的颜色。
                 font=None,             ## 设置字体，包括'courier', 'times', 'arial'。
                 shadow=False,          ## 为文本添加黑色阴影。
                 )

************ 设置标量条 (scalar_bar) ************
## 添加标量条
plotter.add_scalar_bar(title="cluster",       ## 设置标题。
                       title_font_size=20,    ## 设置标题字体的大小。
                       label_font_size=12,    ## 设置标签字体的大小。
                       italic=False,          ## 设置字体为斜体。
                       bold=True,             ## 设置字体为粗体。
                       color="white",         ## 设置字体颜色。
                       font_family="arial",   ## 设置字体，包括'courier', 'times', 'arial'。
                       vertical=True,         ## 设置垂直或水平标量条。(True为垂直)
                       fmt="%Id",             ## 标签的 printf 格式。
                       n_labels=0,            ## 用于标量条的标签数。(对于分类数据必须设置为0)
                       interactive=True,      ## 在交互界面是否可以手动调整scaler bar。(多子图不适用)
                       position_x=0.1,        ## scaler bar在x轴上的坐标位置(0-1之间)
                       position_y=0           ## scaler bar在y轴上的坐标位置(0-1之间)
                       )

## 删除标量条
plotter.remove_scalar_bar(title=None,     ## title指要移除的标量条的标题，如果有多个标量条则为必需项。
                          render=True     ## 是否在标量条移除时渲染。将此设置为 False 则在移除标量条时停止渲染窗口渲染。(一般保持render=True)
                          )



'''













