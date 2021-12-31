'''
Python-matplotlib「刻度(ticker)」 的使用方法之Tick formatters
Tick formatters主要设置刻度标签形式，主要对绘图刻度标签定制化需求时，matplotlib 可支持修改的刻度标签形式如下：

定位器	                解释说明
NullFormatter	        刻度线上没有标签。
IndexFormatter	        从标签列表中设置刻度标签。
FixedFormatter	        手动设置标签字符串。
FuncFormatter	        用户定义的功能设置标签。
StrMethodFormatter      使用字符串方法设置刻度标签。
FormatStrFormatter      使用旧式的sprintf格式字符串。
ScalarFormatter	        标量的默认格式：自动选择格式字符串。
LogFormatter	        Log对数形式的刻度标签。
LogFormatterExponent	使用exponent=log_base（value）形式的刻度标签。
LogFormatterMathtext	使用Math文本使用exponent = log_base（value）格式化对数轴的值。
LogitFormatter	        概率格式器。
PercentFormatter	    将标签格式化为百分比。
'''
import matplotlib.pyplot as plt
from matplotlib import ticker

def setup(ax, title):
    """Set up common parameters for the Axes in the example."""
    # only show the bottom spine
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')

    # define tick positions
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5, labelsize=10)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')

fig0, axs0 = plt.subplots(2, 1, figsize=(8, 2))
fig0.suptitle('Simple Formatting')


setup(axs0[0], title="'{x} km'")
axs0[0].xaxis.set_major_formatter('{x} km')


setup(axs0[1], title="lambda x, pos: str(x-5)")
axs0[1].xaxis.set_major_formatter(lambda x, pos: str(x-5))

fig0.tight_layout()


# The remaining examples use Formatter objects.

fig1, axs1 = plt.subplots(7, 1, figsize=(8, 6))
fig1.suptitle('Formatter Object Formatting')

# Null formatter
setup(axs1[0], title="NullFormatter()")
axs1[0].xaxis.set_major_formatter(ticker.NullFormatter())

# StrMethod formatter
setup(axs1[1], title="StrMethodFormatter('{x:.3f}')")
axs1[1].xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.3f}"))


# FuncFormatter can be used as a decorator
@ticker.FuncFormatter
def major_formatter(x, pos):
    return f'[{x:.2f}]'


setup(axs1[2], title='FuncFormatter("[{:.2f}]".format')
axs1[2].xaxis.set_major_formatter(major_formatter)

# Fixed formatter
setup(axs1[3], title="FixedFormatter(['A', 'B', 'C', ...])")
# FixedFormatter should only be used together with FixedLocator.
# Otherwise, one cannot be sure where the labels will end up.
positions = [0, 1, 2, 3, 4, 5]
labels = ['A', 'B', 'C', 'D', 'E', 'F']
axs1[3].xaxis.set_major_locator(ticker.FixedLocator(positions))
axs1[3].xaxis.set_major_formatter(ticker.FixedFormatter(labels))

# Scalar formatter
setup(axs1[4], title="ScalarFormatter()")
axs1[4].xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))

# FormatStr formatter
setup(axs1[5], title="FormatStrFormatter('#%d')")
axs1[5].xaxis.set_major_formatter(ticker.FormatStrFormatter("#%d"))

# Percent formatter
setup(axs1[6], title="PercentFormatter(xmax=5)")
axs1[6].xaxis.set_major_formatter(ticker.PercentFormatter(xmax=5))

fig1.tight_layout()
plt.show()