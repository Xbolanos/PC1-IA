"""
Receive the name of the xlsx file and returns
the csv file with the properties from 2011
"""

rows = [
    4, 5, 6, 7, 8, 9, 13,
    14, 15, 16, 21, 23,
    24, 25, 27, 28, 29,
    30, 31, 32, 33, 37,
    38, 40, 41, 42, 46,
    47, 48, 49, 50
]
colums = [
    8, 11, 14, 17, 20,
    23, 26, 29, 32, 35,
    38, 41, 44, 47, 50,
    53, 56, 59, 62, 65
]


def read_xls_properties(file):

    import xlrd
    import csv

    workbook = xlrd.open_workbook(str(file))

    with open("properties.csv", "w", newline='') as file:
        for i in range(1, 8):

            worksheet = workbook.sheet_by_index(i)
            writer = csv.writer(file, delimiter=",")

            for col in range(worksheet.ncols):

                row = []
                if (col_idx in colums):
                    for row_idx in rows:

                        row += [worksheet.cell(row_idx, col_idx).value]

                    writer.writerow(row)

    print("CSV file generated")
