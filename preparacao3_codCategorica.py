import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df = pd.read_csv('dados/clientes-v2-tratado.csv')

print(df.head())

# Codificação One-Hot para 'estado_civil'
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)
print('\nDataFraem após codificação One-Hot para "estado_civil"\n', df.head())

# Codificação ordinal para 'nível_educacao'
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-Graduação': 4}
df['nivel_educacao_ordem'] = df['nivel_educacao'].map(educacao_ordem)
print('\nDataFrame após codificação ordinal para "nivel_educacao"\n', df.head())

# Codificação usando o metodo .cat.codes
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes
print('\nDataFrame após o .cat.codes para "area_atuacao"\n', df.head())

# LabelEncoder para 'estado'
# LabelEncoder converte cada valor único para valores de 0 a n
label_encoder = LabelEncoder()
df['estado_label'] = label_encoder.fit_transform(df['estado'])
print('\nDataFrame após LabelEncoder para "estado"\n', df.head())
