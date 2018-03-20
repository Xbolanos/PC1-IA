"""
Receive the name of the xlsx file and returns the csv file with the datas of "actas de sesion" 
"""
import xlrd
import csv

rows = [
    2,3,4,5,6,7,
    8,9,10,11,
    12,13,14,15,
    16,18,19

]
names_file=[
	"../tofix/ActaSesion1.xlsx",
	"../tofix/ActaSesion2.xlsx",
	"../tofix/ActaSesion3.xlsx",
	"../tofix/ActaSesion4.xlsx",
	"../tofix/ActaSesion5.xlsx",
	"../tofix/ActaSesion6.xlsx",
	"../tofix/ActaSesion7.xlsx",
	"../tofix/ActaSesion8.xlsx",
	"../tofix/ActaSesion9.xlsx",
	"../tofix/ActaSesion10.xlsx",
	"../tofix/ActaSesion11.xlsx",
	"../tofix/ActaSesion12.xlsx",
]
def read_all_files():

	for i in names_file:
		read_xls_properties (i)

def read_xls_properties (file):
	
	print(str(file))
	name_file=file.split("/")[2].split(".")[0]+".csv"
	print(name_file)
	workbook = xlrd.open_workbook(str(file))
	print("abrio")
	with open(name_file, "w", newline='') as file:
		worksheet = workbook.sheet_by_index(0)   
		writer = csv.writer(file, delimiter = ",")
		for row_idx in rows:
			row = []
			for col  in range(worksheet.ncols):
				row += [worksheet.cell(row_idx, col).value]
			writer.writerow(row)
	print("CSV file generated")


read_all_files()
