import pandas as pd
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('dados/clientes-v2-tratado.csv')

print(df.head())

# Escolhendo os dados a serem trabalhados
df = df[['idade', 'salario']]

# Normalização - MinMaxScaler
scaler = MinMaxScaler()
df['IdadeMinMax'] = scaler.fit_transform(df[['idade']])
df['SalarioMinMax'] = scaler.fit_transform(df[['salario']])

# Padronização com StandardScaler
scaler = StandardScaler()
df['IdadeStandard'] = scaler.fit_transform(df[['idade']])
df['SalarioStandard'] = scaler.fit_transform(df[['salario']])

# Padronização com RobustScaler
scaler = RobustScaler()
df['IdadeRobust'] = scaler.fit_transform(df[['idade']])
df['SalarioRobust'] = scaler.fit_transform(df[['salario']])

# Print para resumir as padronizações:
# MinMaxScaler
print("MinMaxScaler (de 0 a 1):")
print("IDADE: Min: {:.4f} Mean: {:.4f} Max: {:.4f}".format(df.IdadeMinMax.min(), df.IdadeMinMax.mean(), df.IdadeMinMax.max()))
print("SALÁRIO: Min: {:.4f} Mean: {:.4f} Max: {:.4f}".format(df.SalarioMinMax.min(), df.SalarioMinMax.mean(), df.SalarioMinMax.max()))

# StandardScaler
print('\nStandardScaler (ajusta a média a 0 e o desvio padrão a 1):')
print("IDADE: Min: {:.4f} Mean: {:.18f} Max: {:.4f} Std: {:.4f}".format(df['IdadeStandard'].min(), df['IdadeStandard'].mean(), df['IdadeStandard'].max(), df['IdadeStandard'].std()))
print("SALÁRIO: Min: {:.4f} Mean: {:.18f} Max: {:.4f} Std: {:.4f}".format(df['SalarioStandard'].min(), df['SalarioStandard'].mean(), df['SalarioStandard'].max(), df['SalarioStandard'].std()))

# RobustScaler
print('\nRobustScaler (Ajusta a mediana e IQR):')
print("IDADE: Min: {:.4f} Mean: {:.4f} Max: {:.4f} Std: {:.4f}".format(df['IdadeRobust'].min(), df['IdadeRobust'].mean(), df['IdadeRobust'].max(), df['IdadeRobust'].std()))
print("SALÁRIO: Min: {:.4f} Mean: {:.4f} Max: {:.4f} Std: {:.4f}".format(df['SalarioRobust'].min(), df['SalarioRobust'].mean(), df['SalarioRobust'].max(), df['SalarioRobust'].std()))

print('\n', df.head(20))
