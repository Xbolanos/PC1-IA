

"""
Recibe el nombre de un archivo xls y retorna una lista de listas con los datos
"""
def read_xls (file):
    import xlrd
    
    workbook = xlrd.open_workbook(str(file))

    worksheet = workbook.sheet_by_index(0)

    table = []
    templist = []
    for i in range(worksheet.nrows):
        for j in range(worksheet.ncols):
            templist.append(worksheet.cell(i,j).value)
        table.append(templist)
        templist = []
        
    print(table)


