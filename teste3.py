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

# Definir datas de compra fictícias e preços correspondentes
#datas_compra = ['2022-09-21', '2022-08-15', '2022-03-15']
#precos_compra = [10.29, 9.9, 9.06]


print("000\n")
## Carregar os dados do Excel
df = pd.read_excel("carteira-export.xlsx")  # Substitua "seu_arquivo.xlsx" pelo nome do seu arquivo Excel
print("1")

# Converter a coluna de data para o tipo datetime
df['Data operação'] = pd.to_datetime(df['Data operação'])
print("2")


# Ordernar os dados pela data
df = df.sort_values(by='Data operação')

#start_date = df['Data operação'].iloc[0]
#end_date = df['Data operação'].iloc[-1]


#print(start_date)
#print(end_date)

datas_compra = df['Data operação']
precos_compra = df['Preço unitário']
precos_compra2 = precos_compra.str.replace(",",".")




# Definir o ticket da Amazon
ticker_amzn = 'MXRF11.SA'

# Definir o intervalo de datas para o histórico de preços
start_date = '2019-01-01'
end_date = '2023-12-31'
#start_date = '2022-03-15'
#end_date = '2022-09-21'


# Obter o histórico de preços da Amazon
historical_prices_amzn = get_historical_prices(ticker_amzn, start_date, end_date)


# Convertendo a Series em uma lista
lista_datas_compra = datas_compra.tolist()
lista_precos_compra2 = precos_compra2.tolist()



#print(type(lista_datas_compra))
#print(type(lista_precos_compra2))


# Criar um DataFrame com as datas de compra e preços correspondentes
df_compras = pd.DataFrame({'Data': pd.to_datetime(lista_datas_compra), 'Preço': lista_precos_compra2})
print(df_compras)




# Plotar o gráfico do preço histórico da ação da Amazon
plt.figure(figsize=(20, 16))
plt.plot(historical_prices_amzn.index, historical_prices_amzn.values, label='Preço da Ação')

# Adicionar marcadores para os pontos de compra
plt.scatter(df_compras['Data'], df_compras['Preço'], c='red', label='Compra', marker='o')

#plt.plot(df_compras['Data'], df_compras['Preço'], '-ok')



# Adicionar legendas e título
plt.xlabel('Data')
plt.ylabel('Preço')
plt.title('Preço Histórico da Ação da Amazon (AMZN) e Pontos de Compra')
plt.legend()

# Rotacionar os rótulos do eixo x para melhor visualização
plt.xticks(rotation=45)

# Exibir o gráfico
plt.tight_layout()
plt.show()
