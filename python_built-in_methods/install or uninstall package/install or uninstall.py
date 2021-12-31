'''

下载包：pip install 要下载的包名————从https://pypi.org中找
删除包：pip uninstall 要卸载的包名，而后可以看到一个提示Proceed (y/n)————意思就是问我们是否确定卸载，我们输入y按下回车即可开始卸载
更新包：如果要更新包的版本，要先删除包，然后再下载包
更新pip：py -m pip install --upgrade pip
若pip不小心删除了，下载pip：py -m ensurepip --upgrade

高级操作：
1.若是下载包太慢，可以用清华镜像源，用法如下：
    pip install package -i https://pypi.tuna.tsinghua.edu.cn/simple
2.若是有一些包pip安装失败可以去https://www.lfd.uci.edu/~gohlke/pythonlibs/找到对应python版本的whl文件进行下载
    比如下载Fiona包，我的python版本是3.8.8
    第一步：在https://www.lfd.uci.edu/~gohlke/pythonlibs/中下载Fiona‑1.8.20‑cp38‑cp38‑win_amd64.whl
    第二步：pip install C:\Users\YJJ\Downloads\Fiona‑1.8.20‑cp38‑cp38‑win_amd64.whl
3.如果以上两种办法还没有办法安装，则前往pypi下载包
    比如下载rvlib包
    第一步：在https://pypi.org/project/rvlib/#modal-close上下载压缩包
    第二步：找到压缩包内的rvlib文件和rvlib.egg.info文件添加到C:\python\venv\Lib\site-packages中即可

'''