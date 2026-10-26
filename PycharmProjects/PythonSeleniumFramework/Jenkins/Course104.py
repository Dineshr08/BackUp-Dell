#how to use get and write a data from excel
#first install pip install openpyxl

import openpyxl
book = openpyxl.load_workbook("C:\Jenkins\Selenium.xlsx")#open excel
sheet = book.active #get current opened sheet control
cell = sheet.cell(row=1, column=2) #going to that particular cell
print(cell.value) #getting the cell value
#get cell value based on this way too
print(sheet["A2"].value)
#Writing data to excel
sheet.cell(row=2,column=2).value = "Dinesh"
#getting that writtened value
print(sheet.cell(row=2,column=2).value)
#get max size of row
print(sheet.max_row)
#get max size of column
print(sheet.max_column)