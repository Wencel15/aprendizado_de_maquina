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
