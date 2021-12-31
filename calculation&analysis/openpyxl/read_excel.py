import openpyxl
#读取excel
wb = openpyxl.load_workbook(r'example.xlsx')
#获得excel中所有sheet的名字
listname = wb.sheetnames
#读取excel中第一个sheet
ws = wb[listname[0]]
#根据单元格名称获取单元格内的值
a1_value = ws['A1'].value
#根据表格的行列编号获取单元格的值 ，编号默认从1开始
a2_value = ws.cell(row=1, column=1).value
#获取表格最大的行编号
max_row_num = ws.max_row
#获取表格最大的列编号
max_column_num = ws.max_column
#获取A列到C列到值
for column in ws["A:C"]:
    for cell in column:
        print(cell.value)
print(' ')
#获取所有列的值
for col in ws.iter_cols():
    for cell in col:
        print(cell.value)
#获取第一行到第三行的值
for row in ws[1:3]:
    for cell in row:
        print(cell.value)
print(' ')
#获取所有行的值
for row in ws.iter_rows():
    for cell in row:
        print(cell.value)



