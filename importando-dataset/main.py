import pandas as pd

# Carregando um dataset no formato csv
# Por padrão o pandas utiliza a "," como separador
data = pd.read_csv('./GasPricesinBrazil_2004-2019.csv', sep=';')

# Exibindo os dados da "cabeça"
# Por padrão mostra as 5 primeiras linhas, mas pode especificar
print(data.head(10))

# Exibindo informações gerais do dataset
print(data.info())

# Exibindo as dimensões do Dataframe (n° linhas x n° colunas)
print(f'O Dataframe possui {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/atributos/variáveis')

# Criando um Dataframe
# Passa um dict onde as keys são as colunas e os valores são as linhas
personagens_df = pd.DataFrame({
    'nome': ['Luke Skywlaker', 'Yoda', 'Palpatine'],
    'idade': [16, 1000, 70],
    'peso': [70, 15, 60],
    'eh_jedi': [True, True, True]
})

print(personagens_df.info())

# Exbindo as colunas e convertendo para list
print(personagens_df.columns)
print(list(personagens_df.columns))

# Renomeando colunas, cria uma cópia do Dataframe
personagens_df_rename = personagens_df.rename(columns={
    'nome': 'Nome Completo',
    'idade': 'Idade'
})

print(personagens_df_rename)

# Renomeando colunas, mas alterando o Dataframe original (inplace=True)
personagens_df.rename(columns={'nome': 'Nome Completo', 'idade': 'Idade'}, inplace=True)

print(personagens_df)

# Renomeando colunas de uma única vez usando list
personagens_df.columns = ['NOME', 'IDADE', 'PESO', 'EH_JEDI']

print(personagens_df)