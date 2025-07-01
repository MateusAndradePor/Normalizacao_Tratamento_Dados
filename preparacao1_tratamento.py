import pandas as pd

df = pd.read_csv('dados/clientes-v2.csv')

#Verificação e tratamentos iniciais:
print (df.head())
print (df.tail())
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

#Verificação inicial:
print('Verificação inicial:\n')
print(df.info())

print('Análise de dados nulos:\n', df.isnull().sum())
print('% de campos nulos:\n', df.isnull().mean() * 100)

#Removendo campos nulos
df.dropna(inplace=True)
print('Confirmação de remoção dos dados nulos:\n', df.isnull().sum())

print('Análise de dados duplicados:\n', df.duplicated().sum())
print('Análise de dados únicos:\n', df.nunique())

print('Estatísticas dos dados:\n', df.describe())

# Escolhendo os dados do novo DataFrame: (sem dados de identificação)
df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head().to_string())

df.to_csv('dados/clientes-v2-tratado.csv', index=False)
.