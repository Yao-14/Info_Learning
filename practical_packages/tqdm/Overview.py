'''
Tqdm 是一个快速，可扩展的Python进度条，可以在 Python 长循环中添加一个进度提示信息，用户只需要封装任意的迭代器 tqdm(iterator)。

对进度条进行更加详细的定制，可以实例化一个tqdm类：
    实例化tqdm类比较常用的参数：
        iterable（第一个参数）：一个可迭代对象
        desc：对进度条的描述，会显示在进度条前边
        total：预期的总迭代次数（默认会等于iterable的总次数，如果可数的话）
        ncols：总长度
        mininterval：最小的更新时间间隔，默认为0.1
        maxinterval：最大的更新时间间隔，默认为10
    一个tqdm实例的常用方法：
        set_description：设置显示在进度条前边的内容
        set_postfix：设置显示在进度条后边的内容
        update：对进度进行手动更新
        close：关闭进度条实例，实际上，最好在使用完一个tqdm类的实例后使用 close 方法清理资源，就像使用open打开的文件一样，从而释放内存。
               因为一个实例化的tqdm也需要在使用完毕后通过close方法清理资源，这和打开一个文件进行处理是很类似的，因此同样可以使用with语句，让其在执行完后自动清理，就不再需要使用close方法手动关闭了：

'''
from tqdm import trange
import time
with open('J.regia.chr.genome.fa', 'r') as raw_file:
    content = [i for i in raw_file.readlines()]
    site_of_chr_list = [n for n, value in enumerate(content) if value.startswith('>')]
    site_of_chr_list.append(len(content))
    chr_list = [[i, j] for i, j in zip(site_of_chr_list[:-1], site_of_chr_list[1:])]
    # 实例化一个tqdm类,注意total的数量跟for循环中的另一个参数数量相同，即chr_list中的数量和total的数量一样
    p_bar = trange(100, desc="A Processing Bar Sample: ",postfix='这是进度条的后缀', total=15, ncols=100)
    for i,j in zip(chr_list, p_bar):
        chr = content[i[0]]
        new_file_content = content[i[0]:i[1]]
        p_bar.set_description("Processing %s" % chr.strip('\n'))
        time.sleep(0.1)
    p_bar.close()