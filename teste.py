#Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
from pandas_datareader import data
import matplotlib.pyplot as plt

#Escolhendo os ativos
acoes = ['GOLL4.SA', 'CVCB3.SA', 'WEGE3.SA', 'MGLU3.SA', 'TOTS3.SA', 'BOVA11.SA']

#Buscando os dados na web e visualizando os 5 primeiros e os 5 últimos
acoes_df = pd.DataFrame()
for acao in acoes:
    acoes_df[acao] = data.DataReader(acao, data_source='yahoo', start='2015-01-01')['Close']
acoes_df

#Renomeando as colunas e conferindo
acoes_df = acoes_df.rename(columns={'GOLL4.SA': 'GOL', 'CVCB3.SA': 'CVC', 'WEGE3.SA': 'WEGE', 'MGLU3.SA': 'MGLU', 'TOTS3.SA': 'TOTS', 'BOVA11.SA': 'BOVA'})
acoes_df.head()

#Apagando os valores Nulos
acoes_df.dropna(inplace=True)

#Transferindo o arquivo para formato csv e depois o lendo
acoes_df.to_csv('acoes.csv')
acoes_df = pd.read_csv('acoes.csv')

#Gráfico em linha dos preços históricos das ações
acoes_df.plot(x = 'Date', figsize = (15,7), title = 'Histórico do preço das ações');