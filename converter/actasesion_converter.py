"""
Receive the name of the xlsx file and returns the csv file with the datas of "actas de sesion" 
"""
import xlrd
import csv

rows = [
    2,3,4,5,6,7,
    8,9,10,11,
    12,13,14,15,
    17,18

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
	rows_new_file=[]

	for i in names_file:
		if(names_file.index(i)==0):
			rows_new_file=read_xls_properties (i)
			#print(rows_new_file)
		else:
			#print("holi")
			rows_new_file=concatenate_rows(rows_new_file, read_xls_properties (i))
	print(rows_new_file)
	with open("ActaSesionCompleta.csv", "w", newline='') as file:
		
		writer = csv.writer(file, delimiter = ",")
		for row in rows_new_file:
			writer.writerow(row)
	


def concatenate_rows(array1, array2):
	array_aux=[]
	print(array2)
	for i in array1:
		print(array1.index(i))
		print(array2[array1.index(i)][1:len(array2[array1.index(i)])])
		array_aux+=[i+array2[array1.index(i)][1:len(array2[array1.index(i)])]]
	return array_aux



def read_xls_properties (file):
	rows_new_file=[]
	print(str(file))
	file_aux=str(file)
	name_file=file.split("/")[2].split(".")[0]+".csv"
	workbook = xlrd.open_workbook(str(file))
	
	with open(name_file, "w", newline='') as file:
		worksheet = workbook.sheet_by_index(0)   
		writer = csv.writer(file, delimiter = ",")
		for row_idx in rows:
			row = []
			for col  in range(worksheet.ncols):
				row += [worksheet.cell(row_idx, col).value]

			
			rows_new_file+=[row]
		



			#print(rows_new_file)

			writer.writerow(row)
	print("CSV file generated")

	return rows_new_file


read_all_files()
