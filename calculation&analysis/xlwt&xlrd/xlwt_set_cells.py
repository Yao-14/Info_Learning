import xlwt
workbook = xlwt.Workbook(encoding='utf8')
sheet1 = workbook.add_sheet('sheet1')

#单元格格式设置
style = xlwt.XFStyle() #创建一个样式对象，初始化样式 style
#Font：字体设置
font = xlwt.Font()
font.name = 'Calibri' # 设置字体
font.colour_index = 2 # 设置字体颜色 0黑色，1白色，2红色，3绿色，4深蓝色，5黄色，6粉紫色，7天蓝色
font.height = 400 # 字体大小
font.bold = True # 字体是否为粗体
font.italic = True # 字体是否为斜体
font.underline = True # 字体是否有下划线
font.struck_out =True # 字体中是否有横线
style.font = font
#Alignment：水平位置设置
alignment = xlwt.Alignment()
alignment.horz = 1      # 设置水平位置，0是左对齐，1是居中，2是右对齐
style.alignment = alignment
#Border：边框设置
borders = xlwt.Borders()
# 细实线:1，小粗实线:3.2寻找位于变异区段的基因，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7
# 大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13
borders.left = 1
borders.right = 2
borders.top = 3
borders.bottom = 4
#边框颜色设置 0黑色，1白色，2红色，3绿色，4深蓝色，5黄色，6粉紫色，7天蓝色
borders.left_colour = 2
borders.right_colour = 3
borders.top_colour = 4
borders.bottom_colour = 5
style.borders = borders
#Background：背景设置
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 4  # 给背景颜色赋值 0黑色，1白色，2红色，3绿色，4深蓝色，5黄色，6粉紫色，7天蓝色
style.pattern = pattern  # 把背景颜色加到表格样式里去

sheet1.write(0,0,'课程',style)

#例如字体的设置
def set_stylefont(name, height,colour,bold=True,italic = True,underline = True,struck_out = True):
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()
    font.name = name  # 设置字体
    font.colour_index = colour  # 设置字体颜色 0黑色，1白色，2红色，3绿色，4深蓝色，5黄色，6粉紫色，7天蓝色
    font.height = height  # 字体大小
    font.bold = bold  # 字体是否为粗体
    font.italic = italic  # 字体是否为斜体
    font.underline = underline # 字体是否有下划线
    font.struck_out = struck_out # 字体中是否有横线
    style.font = font
    return style
sheet1.write(0,1,'课程',set_stylefont('Calibri',300,3,False,True,True,True))
workbook.save(r'/Users/a15967101830/PycharmProjects/study1/上课/1.excel处理/tryexcel1.xls')