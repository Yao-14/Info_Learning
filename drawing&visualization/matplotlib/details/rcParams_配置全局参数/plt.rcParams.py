import matplotlib.pyplot as plt

'''对于同时绘制多个子图，可以通过设置全局变量来实现一次性设置所有子图中各个变量的格式（如设置所有ticks的字体格式为'Arial'）

plt.rcParams包含的可以设置参数：

backend
backend_fallback
toolbar
interactive
timezone
_internal.classic_mode

webagg相关: webagg.port ;webagg.address ;webagg.open_in_browser ;webagg.port_retries

lines相关:  lines.linewidth ;lines.linestyle ;lines.color ;lines.marker ;lines.markerfacecolor ;lines.markeredgecolor ;
           lines.markeredgewidth ;lines.markersize ;lines.antialiased ;lines.dash_joinstyle ;lines.solid_joinstyle ;
           lines.dash_capstyle ;lines.solid_capstyle ;lines.dashed_pattern ;lines.dashdot_pattern ;lines.dotted_pattern ;
           lines.scale_dashes ;markers.fillstyle

pcolor相关: pcolor.shading ;pcolormesh.snap

patch相关:  patch.linewidth ;patch.edgecolor ;patch.force_edgecolor ;patch.facecolor ;patch.antialiased

hatch相关:  hatch.color ;hatch.linewidth

hist相关:   hist.bins

boxplot相关:boxplot.notch ;boxplot.vertical ;boxplot.whiskers ;boxplot.bootstrap ;boxplot.patchartist ;boxplot.showmeans ;
           boxplot.showcaps ;boxplot.showbox ;boxplot.showfliers ;boxplot.meanline ;boxplot.flierprops.color ;
           boxplot.flierprops.marker ;boxplot.flierprops.markerfacecolor ;boxplot.flierprops.markeredgecolor ;
           boxplot.flierprops.markeredgewidth ;boxplot.flierprops.markersize ;boxplot.flierprops.linestyle ;
           boxplot.flierprops.linewidth ;boxplot.boxprops.color ;boxplot.boxprops.linewidth ;boxplot.boxprops.linestyle ;
           boxplot.whiskerprops.color ;boxplot.whiskerprops.linewidth ;boxplot.whiskerprops.linestyle ;boxplot.capprops.color ;
           boxplot.capprops.linewidth ;boxplot.capprops.linestyle ;boxplot.medianprops.color ;boxplot.medianprops.linewidth ;
           boxplot.medianprops.linestyle ;boxplot.meanprops.color ;boxplot.meanprops.marker ;boxplot.meanprops.markerfacecolor ;
           boxplot.meanprops.markeredgecolor ;boxplot.meanprops.markersize ;boxplot.meanprops.linestyle ;boxplot.meanprops.linewidth

font相关:   font.family ;font.style ;font.variant ;font.stretch ;font.weight ;font.size ;font.serif ;font.sans-serif ;
           font.cursive ;font.fantasy ;font.monospace

text相关:   text.color ;text.usetex ;text.latex.preamble ;text.latex.previe ;text.hinting ;text.hinting_factor ;
           text.kerning_factor ;text.antialiased

mathtext相关: mathtext.cal ;mathtext.rm ;mathtext.tt ;mathtext.it ;mathtext.bf ;mathtext.sf ;mathtext.fontset ;
             mathtext.default ;mathtext.fallback_to_cm ;mathtext.fallback

image相关:    image.aspect ;image.interpolation ;image.cmap ;image.lut ;image.origin ;image.resample ;image.composite_image

contour相关:  contour.negative_linestyle ;contour.corner_mask ;contour.linewidth

errorbar相关: errorbar.capsize

xaxis相关:    xaxis.labellocation

yaxis相关:    yaxis.labellocation

axes相关:     axes.axisbelow ;axes.facecolor ;axes.edgecolor ;axes.linewidth ;axes.spines.left ;axes.spines.right ;
             axes.spines.bottom ;axes.spines.top ;axes.titlesize ;axes.titlelocation ;axes.titleweight ;axes.titlecolor ;
             axes.titley ;axes.titlepad ;axes.grid ;axes.grid.which ;axes.grid.axis ;axes.labelsize ;axes.labelpad ;
             axes.labelweight ;axes.labelcolor ;axes.formatter.limits ;axes.formatter.use_locale ;axes.formatter.use_mathtext ;
             axes.formatter.min_exponent ;axes.formatter.useoffset ;axes.formatter.offset_threshold ;axes.unicode_minus ;
             axes.prop_cycle ;axes.autolimit_mode ;axes.xmargin ;axes.ymargin ;axes.zmargin

polaraxes相关:polaraxes.grid

axes3d相关:   axes3d.grid

scatter相关:  scatter.marker ;scatter.edgecolors

date相关:     date.epoch ;date.autoformatter.year ;date.autoformatter.month ;date.autoformatter.day ;date.autoformatter.hour ;
             date.autoformatter.minute ;date.autoformatter.second ;date.autoformatter.microsecond ;date.converter ;date.interval_multiples

legend相关:   legend.fancybox ;legend.loc ;legend.numpoints ;legend.scatterpoints ;legend.fontsize ;legend.title_fontsize ;
             legend.markerscale ;legend.shadow ;legend.frameon ;legend.framealpha ;legend.borderpad ;legend.labelspacing ;
             legend.handlelength ;legend.handleheight ;legend.handletextpad ;legend.borderaxespad ;legend.columnspacing ;
             legend.facecolor ;legend.edgecolor

xtick相关:    xtick.top ;xtick.bottom ;xtick.labeltop ;xtick.labelbottom ;xtick.major.size ;xtick.minor.size ;xtick.major.width ;
             xtick.minor.width ;xtick.major.pad ;xtick.minor.pad ;xtick.color ;xtick.labelcolor ;xtick.minor.visible ;
             xtick.minor.top ;xtick.minor.bottom ;xtick.major.top ;xtick.major.bottom ;xtick.labelsize ;xtick.direction ;xtick.alignment

ytick相关:    ytick.left ;ytick.right ;ytick.labelleft ;ytick.labelright ;ytick.major.size ;ytick.minor.size ;ytick.major.width ;
             ytick.minor.width ;ytick.major.pad ;ytick.minor.pad ;ytick.color ;ytick.labelcolor ;ytick.minor.visible ;
             ytick.minor.left ;ytick.minor.right ;ytick.major.left ;ytick.major.right ;ytick.labelsize ;ytick.direction ;ytick.alignment

grid相关:     grid.color ;grid.linestyle ;grid.linewidth ;grid.alpha

figure相关:   figure.titlesize ;figure.titleweight ;figure.figsize ;figure.dpi ;figure.facecolor ;figure.edgecolor ;
             figure.frameon ;figure.autolayout ;figure.max_open_warning ;figure.raise_window ;figure.subplot.left ;
             figure.subplot.right ;figure.subplot.bottom ;figure.subplot.top ;figure.subplot.wspace ;figure.subplot.hspace ;
             figure.constrained_layout.use ;figure.constrained_layout.hspace ;figure.constrained_layout.wspace ;
             figure.constrained_layout.h_pad ;figure.constrained_layout.w_pad
 
savefig相关:  savefig.dpi ;savefig.facecolor ;savefig.edgecolor ;savefig.orientation ;savefig.jpeg_quality ;savefig.format;
             savefig.bbox ;savefig.pad_inches ;savefig.directory ;savefig.transparent

tk相关:       tk.window_focus

ps相关:       ps.papersize ;ps.useafm ;ps.usedistiller ;ps.distiller.res ;ps.fonttype

pdf相关:      pdf.compression ;pdf.inheritcolor ;pdf.use14corefonts ;pdf.fonttype ;pgf.texsystem ;pgf.rcfonts ;pgf.preamble

svg相关:      svg.image_inline ;svg.fonttype ;svg.hashsalt

docstring相关:docstring.hardcopy

path相关:     path.simplify ;path.simplify_threshold ;path.snap ;path.sketch ;path.effects

agg.path相关: agg.path.chunksize

keymap相关:   keymap.fullscreen ;keymap.home ;keymap.back ;keymap.forward ;keymap.pan ;keymap.zoom ;keymap.save ;keymap.quit ;
             keymap.quit_all ;keymap.grid ;keymap.grid_minor ;keymap.yscale ;keymap.xscale ;keymap.all_axes ;keymap.help ;keymap.copy

animation相关:animation.html ;animation.embed_limit ;animation.writer ;animation.codec ;animation.bitrate ;animation.frame_format ;
             animation.html_args ;animation.ffmpeg_path ;animation.ffmpeg_args ;animation.avconv_path ;animation.avconv_args ;
             animation.convert_path ;animation.convert_args

plt.rcParams各个参数设置参考————print(plt.rcParams.keys())

#plt.rcParams的使用方法1————一一设置(以设置font为例,必须设置在fig之前）：
plt.rcParams['font.weight'] = 'semibold'
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.style'] = 'normal'
plt.rcParams['font.size'] = 15

#plt.rcParams的使用方法2————一次设置多个参数(以设置font为例,必须设置在fig之前）：
plt.rc('font',weight='semibold',family='Arial',style='normal',size=15)
'''

plt.rc('font',weight='semibold',family='Arial',style='normal',size=15)
print(plt.rcParams.keys())
fig,axes = plt.subplots(2,2,figsize=[10,10],dpi=100)
plt.tight_layout()
plt.show()