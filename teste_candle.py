import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=UserWarning) 

import pandas as pd
import yfinance as yf
import mplfinance as mpf

# Função para obter o histórico de preços de uma ação
def get_historical_prices(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date)
    return df

# Definir o ticket da Amazon
ticker_amzn = 'MXRF11.SA'

# Definir o intervalo de datas para o histórico de preços
start_date = '2019-01-01'
end_date = '2023-12-31'

# Obter o histórico de preços da Amazon
historical_prices_amzn = get_historical_prices(ticker_amzn, start_date, end_date)

# Carregar os dados do Excel
df = pd.read_excel("carteira-export.xlsx")  # Substitua "carteira-export.xlsx" pelo nome do seu arquivo Excel

# Converter a coluna de data para o tipo datetime
df['Data operação'] = pd.to_datetime(df['Data operação'])

# Converter a coluna de preço para float, removendo vírgulas
df['Preço unitário'] = df['Preço unitário'].str.replace(',', '.').astype(float)

# Ordenar os dados pela data
df = df.sort_values(by='Data operação')

# Criar um DataFrame com as datas de compra e preços correspondentes
df_compras = df[['Data operação', 'Preço unitário']].rename(columns={'Data operação': 'Date', 'Preço unitário': 'Close'})

# Converter o DataFrame de compras para o formato esperado pela função addplot
df_compras.set_index('Date', inplace=True)

# Verificar se as datas de compra estão presentes no intervalo do histórico de preços
df_compras = df_compras[df_compras.index.isin(historical_prices_amzn.index)]

# Criar um gráfico de candlestick do preço histórico da ação da Amazon
mpf.plot(historical_prices_amzn,
         type='candle',
         style='charles',
         ylabel='Price',
         ylabel_lower='Volume',
         title='Preço Histórico da Ação da Amazon (MXRF11.SA) e Pontos de Compra',
         alines=dict(alines=[(idx, row['Close']) for idx, row in df_compras.iterrows()], colors=['r'], linewidths=[1]),
         )

