import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=UserWarning) 

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Função para obter o histórico de preços de uma ação
def get_historical_prices(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date)
    return df['Close']

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
df_compras = df[['Data operação', 'Preço unitário']].rename(columns={'Data operação': 'Data', 'Preço unitário': 'Preço'})

# Plotar o gráfico do preço histórico da ação da Amazon e os pontos de compra
plt.figure(figsize=(20, 16))
plt.plot(historical_prices_amzn.index, historical_prices_amzn.values, label='Preço da Ação')
plt.scatter(df_compras['Data'], df_compras['Preço'], c='red', label='Compra', marker='o')

# Adicionar anotações com o preço de compra aos pontos de compra
for i, row in df_compras.iterrows():
    plt.annotate(f'{row["Preço"]:.2f}', (row['Data'], row['Preço']), textcoords="offset points", xytext=(0,10), ha='center')

# Adicionar legendas e título
plt.xlabel('Data')
plt.ylabel('Preço')
plt.title('Preço Histórico da Ação da (MXRF11.SA) e Pontos de Compra')
plt.legend()

# Rotacionar os rótulos do eixo x para melhor visualização
plt.xticks(rotation=45)

# Exibir o gráfico
plt.tight_layout()
plt.show()
