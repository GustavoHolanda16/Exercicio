from openpyxl import Workbook, load_workbook 
arquivo = load_workbook('planilha.xlsx')
for i in arquivo:
    print(i)
for i in range(10):
    planilha ['A']=input()