'''
一、python处理excel文件两种方式（行数最大65535）：
1.读取excel文件
当我们需要读取excel文件的时候，需要用到xlrd库。

3.2寻找位于变异区段的基因.写出excel文件
当我们需要写出excel文件的时候，需要用到xlwt库。（xlwt不能重复覆盖一个单元格的值，而openpyxl可以）
'''

#读取excel
import xlrd
#打开excel
rb = xlrd.open_workbook('/上课/1.excel处理/例子/Juredeletion.xls')
#获得excel中所有sheet的名字
listname = rb.sheet_names()
print(listname)
#打开excel中名字为2的sheet（三种方法）
sheetrd1 = rb.sheet_by_name('3.2寻找位于变异区段的基因')
print(sheetrd1)
#获取一个sheet中的行数、列数、名字———————编号默认从0开始
row = sheetrd1.nrows #获得行数
col = sheetrd1.ncols #获得列数
name = sheetrd1.name #获得名字
print(row,col,name)
#获取sheet中每一行/每一列的数据——输出的是一个列表
for i in range(row):
    sheetrd1.row_values(i)
for j in range(col):
    sheetrd1.col_values(j)
#获得sheet中某一个单元格的值
val001 = sheetrd1.cell(0, 1).value
val002 = sheetrd1.row(0)[0].value
print(val001,val002)

#写出excel
import xlwt
#创建一个excel
workbook = xlwt.Workbook(encoding='utf8')
#在excel中添加sheet并命名为sheet1、sheet2
sheet1 = workbook.add_sheet('sheet1')
sheet2 = workbook.add_sheet('sheet2')
#在表中写入数据——（0，0）用于定位写入哪一个空格，后面接写入的内容
sheet1.write(0,0,'课程')
sheet1.write(0,1,'上课时间')
listtype = ['语文','数学','英语','科学']
listtime = ['一点','两点','三点','四点']
for i in range(1,len(listtype)+1):
    sheet1.write(i,0,listtype[i-1])
for j in range(1,len(listtime)+1):
    sheet1.write(j,1,listtype[j-1])

#保存为xls文件
workbook.save(r'/Users/a15967101830/PycharmProjects/study1/上课/1.excel处理/tryexcel.xls')






