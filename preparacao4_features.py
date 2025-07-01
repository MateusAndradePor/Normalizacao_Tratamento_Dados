import pandas as pd
import numpy as np
from scipy import stats

# Criação do DataFrame
pd.set_option('display.width', None)
df = pd.read_csv('dados/clientes-v2-tratado.csv')

print(df.head())

# Transformação Logarítmica:
df['salario_log'] = np.log1p(df['salario']) #log1p é usado para evitar problemas com valores zero
print('\nDataFrame com a transformação logarítmica para "salário":\n', df.head())

# Transformação Box-Cox:
df['salario_boxcox'], _ = stats.boxcox(df['salario'] + 1)
print('\nDataFrame com a transformação box-cox para "salário":\n', df.head())

# Codificação de frequência para 'estado':
estado_freq = df['estado'].value_counts()/len(df)
df['estado_freq'] = df['estado'].map(estado_freq)
print('\nDataFrame com a transformação de frequência para "estado":\n', df.head())

# Interações
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']
print('\nDataFrame com a interação entre "idade" e "numero_filhos":\n', df.head())
