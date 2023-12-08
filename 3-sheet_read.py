from openpyxl import load_workbook

# Acessando area de trabalho e planilha
workbook = load_workbook("data/pivot_table.xlsx")
sheet = workbook["Relatório"]

# Acessando Valor Especifico
print(sheet["B3"].value)

#Interado Valores por loop
for i in range(2,6):
    year = sheet["A%s" %i].value
    am = sheet["B%s" %i].value
    bt = sheet["C%s" %i].value
    print("{0} o Aston Martin vendeu {1}, e o Bentley vendeu {2}".format(year, am, bt))