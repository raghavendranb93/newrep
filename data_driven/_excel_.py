import xlrd

def locators(sheetname):
    wb = xlrd.open_workbook(r"C:\Users\RAGHAVENDRA\Desktop\trainee\objects (1).xls")
    ws = wb.sheet_by_name(sheetname)
    row_count = ws.nrows
    locators = { }
    for i in range(1, row_count):      # for i in range(6)
        row_data = ws.row_values(i)
        locators[row_data[0]] = (row_data[1], row_data[2])
    return locators

def headers(sheetname, testcase):
    """retuns the headers of the testcase in comma seprated string"""
    wb = xlrd.open_workbook(r"C:\Users\RAGHAVENDRA\Desktop\trainee\testdata (1).xls")
    ws = wb.sheet_by_name(sheetname)
    row_count = ws.nrows
    for i in range(0, row_count):
        row = ws.row_values(i)
        if row[0] == testcase:
            headers = ws.row_values(i-1)
            # Removing those items with empty string or empty columns
            headers = [ header for header in headers if header ]
            return ",".join(headers[2:])

def data(sheetname, testcase):
    wb = xlrd.open_workbook(r"C:\Users\RAGHAVENDRA\Desktop\trainee\testdata (1).xls")
    ws = wb.sheet_by_name(sheetname)
    row_count = ws.nrows
    final_data = [ ]
    for i in range(0, row_count):
        row = ws.row_values(i)
        if row[0] == testcase:
                data = ws.row_values(i)
                # Removing those items with empty string or empty columns
                data = [ row for row in data if row ]
                # Not interested in test scipt name, so slicing everything from 1st index
                data = data[1:]
                # Not interested in all the rows, but the one which has "execute" column as "Yes"
                if data[0].upper() == "YES":
                    final_data.append(tuple(data[1:]))
    return final_data
                
                






































































# def read_locators(sheetname):
#     """retuns the headers of the testcase in comma seprated string"""
#     wb = xlrd.open_workbook("./data_files/objects.xls")
#     ws = wb.sheet_by_name(sheetname)
#     total_rows = ws.nrows
#     objects = { }
#     for index in range(1, total_rows):
#         row = ws.row_values(index)
#         objects[row[0]] = (row[1], row[2])
#     return objects

# def read_headers(sheetname, testcase):
#     """Returns a dictionary with field name as key and locator type and locator value as value (tuple)"""
#     wb = xlrd.open_workbook("./data_files/testdata.xls")
#     ws = wb.sheet_by_name(sheetname)
#     total_rows = ws.nrows
#     for index in range(total_rows):
#         row = ws.row_values(index)
#         if row[0] == testcase:
#             headers = ws.row_values(index-1, 2)
#             return ",".join([  header for header in headers if header ])

# def read_data(sheetname, testcase):
#     """Returns a list of tuples"""
#     wb = xlrd.open_workbook("./data_files/testdata.xls")
#     ws = wb.sheet_by_name(sheetname)
#     total_rows = ws.nrows
#     final_data = [ ]
#     for index in range(total_rows):
#         row = ws.row_values(index)
#         if row[0] == testcase:
#             data = ws.row_values(index, 1)
#             data = [ item for item in data if item ]
#             if data[0].lower() == "yes":
#                 final_data.append(tuple(data[1:]))
#     return final_data