'''
Python运行后，报错：SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

原因：在windows系统当中读取文件路径可以使用\,但是在python字符串中\有转义的含义，如\t可代表TAB，\n代表换行，所以我们需要采取一些方式使得\不被解读为转义字符。

解决方法：一:更换为绝对路径的写法
        "C:\\Users\\renyc"

        二:显式声明字符串不用转义（加r）
        r"C:\Users\renyc"

        三:使用Linux的路径/
        "C:/Users/renyc"
'''