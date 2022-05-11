import xlrd

def read_locators(sheetname):
    wb = xlrd.open_workbook(r"C:\Users\RAGHAVENDRA\Desktop\trainee\objects.xls")
    ws = wb.sheet_by_name(sheetname)
    rows = ws.get_rows()
    headers = next(rows)
    locators = {row[0].value: (row[1].value, row[2].value) for row in rows}
    return locators

# print(read_locators("loginpage"))