import yfinance as yf
tkr = yf.Ticker('AAPL')
hist = tkr.history(period="1y")

# Obtendo dados do indice de ações do site da Stooq
# Com o modulo datetime do Python definimos as datas e depois chamamos o metodo get_data_stooq() para solicitar os dados 

import pandas_datareader.data as pdr
from datetime import date, timedelta
end = date.today()
start = end - timedelta(days=365)
index_data = pdr.get_data_stooq('^SPX', start, end)

#Combinando os dados em um unico DataFrame
#Para evitar sobreposição utilizamos o parametro rsuffix

df = hist.join(index_data, rsuffix = '_idx')

#Filtrando por colunas de preço de fechamento e os volumes

df = df[['Close', 'Volume', 'Close_idx', 'Volume_idx']]
print(df)

# Derivando features de dados contínuos
# Utilizaremos o shift(1) para calcular a mudança precentual diária de cada coluna do DataFrame, salvando os resultados em um novo lote de colunas:

import numpy as np
df['priceRise'] = np.log(df['Close'] / df['Close'].shift(1))
df['volumeRise'] = np.log(df['Volume'] / df['Volume'].shift(1))
df['priceRise_idx'] = np.log(df['Close_idx'] / df['Close_idx'].shift(1))
df['volumeRise_idx'] = np.log(df['Volume_idx'] / df['Volume_idx'].shift(1))
df = df.dropna()

# Agora filtraremos o DataFrame para incluir apenas as colunas novas:

df = df[['priceRise', 'volume_Rise', 'priceRise_idx', 'volumeRise_idx']]

#Gerando a variavél de saida, alterando para shift(-1) a mudança negativa desloca os valores futuros um passo atrás no tempo.

conditions - [
  (df['priceRise'].shift(-1) > 0.01),
  (df['priceRise'].shift(-1) < -0.01)
]
choices = [1, -1]
df['Pred'] = np.select(conditions, choices, default=0)

# Treinando e avaliando o modelo

features = df[['priceRise', 'volumeRise', 'priceRise_idx', 'volumeRise_idx']].to_numpy()
features = np.araund(features, decimals=2)
target = df['Pred'].to_numpy()

#Dividindo os dados em conjuntos de treinamento

from sklearn.model_selection import train_test_split
rows_trains, rows_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(rows_trains, y_trains)

#Acurácia

print(clf.score(rows_test, y_test)


  

