import pandas as pd

# Carregando um dataset no formato csv
# Por padrão o pandas utiliza a "," como separador
data = pd.read_csv('./GasPricesinBrazil_2004-2019.csv', sep=';')

# Exibindo os dados da "cabeça"
# Por padrão mostra as 5 primeiras linhas, mas pode especificar
print(data.head(10))



