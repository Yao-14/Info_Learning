'''
openpyxl模块是一个读写Excel2010以后版本的Python库，openpyxl是一个比较综合的工具，
能够同时读取和修改Excel文档。保存为xlsx文件
'''
import openpyxl
#一.创建Excel文件
wb = openpyxl.Workbook()
#更改默认sheet页的名称
ws = wb.active # 当前打开的sheet页 wb.active
ws.title = "WorkSheetTitle" # 更改默认名称Sheet
#若要作成含多个sheet页的Excel，同时可以设定新建的sheet的位置
ws2 = wb.create_sheet("NewWorkSheet2") # 定义第二个sheet页
ws3 = wb.create_sheet("NewWorkSheet3", 1) # 定义第三个sheet页，并设定该sheet的位置为第二个
wb.save('jcde.xlsx')

#二.单元格赋值
#指定坐标给单元格赋值
ws["A1"] = "HOGE"
ws["B1"] = "FUGA"
#指定行列给单元格赋值
ws.cell(row=1, column=3, value=10)
#一次输出行
rows = [["FirstName", "LastName"],["Tarou", "Tanaka"],["Tarou", "Suzuki"],["Tarou", "Uchiayama"]]
for row in rows:
    ws.append(row)
#单元格内换行
ws['A1'] = "A\nB\nC"
ws['A1'].alignment = openpyxl.styles.Alignment(wrapText=True)
# 保存
wb.save('jcde.xlsx')


#三.设置单元格格式
#设置字体font
from openpyxl.styles import fills,colors,NamedStyle,Font,Side,Border,PatternFill,Alignment,Protection
font = openpyxl.styles.Font(
    size=11,
    bold=True, #加粗
    italic=True,  # 斜体
    color='FFFF00') #字体颜色，FFFFFF白色，000000黑色，FF0000红色，008000绿色，FFFF00黄色，0000FF蓝色，800080紫色 https://www.sioe.cn/yingyong/yanse-rgb-16/
ws["B2"].font = font

#单元格边框border
from openpyxl.styles import Border, Side
border = Border(
    left=Side(
        border_style="thin", #border_style有'hair', 'medium', 'dashDot', 'dotted', 'mediumDashDot', 'dashed', 'mediumDashed', 'mediumDashDotDot', 'dashDotDot', 'slantDashDot', 'double', 'thick', 'thin'
        color="FF0000"), #边框颜色，FFFFFF白色，000000黑色，FF0000红色，008000绿色，FFFF00黄色，0000FF蓝色，800080紫色 https://www.sioe.cn/yingyong/yanse-rgb-16/
    right=Side(
        border_style="thin",
        color="FF0000"),
    top=Side(
        border_style="thin",
        color="FF0000"),
    bottom=Side(
        border_style="thin",
        color="FF0000"))
ws["A3"].border = border

#单元格填充颜色
from openpyxl.styles import PatternFill
fill = PatternFill(fill_type='solid',
                       fgColor='FFFF0000')
ws["B2"].fill = fill

#对齐方式
alignment=Alignment(horizontal='center',#水平'center', 'centerContinuous', 'justify', 'fill', 'general', 'distributed', 'left', 'right'
            vertical='top',#垂直'distributed', 'bottom', 'top', 'center', 'justify'
                    )
ws["B2"].alignment = alignment

# 合并单元格
ws.merge_cells("A1:E1")
ws["A1"] = "HOGE"

#保存为xlsx文件
wb.save('jcde.xlsx')
