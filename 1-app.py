import pandas as pd
# Importação dos dados
data = pd.read_excel("data/VendaCarros.xlsx")

# Listando os primeiros registros
print(data.head())

# Listando os ultimos registros
print(data.tail())

# Contagem de valores por Fabricantes
print(data["Fabricante"].value_counts())