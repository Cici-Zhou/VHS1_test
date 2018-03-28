import xlrd

ExcelFile = xlrd.open_workbook('VHSuser.xlsx')
print(ExcelFile.sheet_names())
sheet = ExcelFile.sheet_by_name('Sheet1')
print (sheet)
cell_A1 = sheet.col_values(1)
print (cell_A1)
cell = sheet.cell(1,0).value
print(int(cell))
