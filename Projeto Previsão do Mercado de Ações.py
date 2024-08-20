#!/usr/bin/env python
# coding: utf-8

# # Projeto Previsão do Mercado de Ações  

# O intuito desse projeto é aprimorar meu conhecimento nos algoritmos de previsão em Machine Learning.

# Para executarmo esse projeto devemos: 1º - Baixar os dados da IBOVESPA; 2º - Limpar os dados e utilizaremos para treinar um modelo; 3º - Realizar testes para descobrir quão bom nosso modelo é; 4º - Adicionar alguns preditores para melhoar nossa precisão; 5º - Passos para continuar melhorando o modelo por conta própria

#  **1º - Baixar os dados da IBOVESPA**

# In[2]:


get_ipython().system('pip install yfinance')


# O pacote "yfinance" chama a API do Yahoo Finance e baixa os preços diários de ações e índices

# In[51]:


import yfinance as yf
import matplotlib.pyplot as plt


# A classe Ticker, permite baixarmos o histórico de preços de um único símbolo

# In[52]:


# Utilizaremos o símbolo 'BVSP', que representa a IBOVESPA
ibvsp = yf.Ticker('^BVSP')


# In[53]:


#Consultar os preços históricos
ibvsp = ibvsp.history(period='max')


# In[54]:


ibvsp


# In[55]:


ibvsp.index


# **2º - Limpeza e visualização dos dados do Mercado de Ações**

# Para conseguirmos ter uma análise melhor do mercado nos últimos tempos vamos plotar o Histórico de Preços da IBOVESPA, nos últimos anos

# In[56]:


ibvsp.plot.line(y='Close', use_index=True)
plt.title('Histórico de Preços IBOVESPA')  
plt.ylabel('Valor de Fechamento') 
plt.xlabel('Anos')
plt.show()  


# In[57]:


# Removemos essas colunas, pois elas são focadas em ações individuais
del ibvsp['Dividends']
del ibvsp['Stock Splits']


# **3º - Configurando nosso alvo para Machine Learning**

# Para atingirmos nosso alvo utilizando machine learning devemos saber o que iremos prever a partir destes dados

# **Alvo**: AMANHÃ O PREÇO IRÁ: AUMENTAR? DIMINUIR?

# Para isso o que tentaremos fazer é dizer que nos dias que a ação subir conseguiremos prever que ela vai subir?

# In[58]:


ibvsp['Tomorrow'] = ibvsp['Close'].shift(-1)


# In[59]:


ibvsp


# Criamos um booleano para saber se o preço de amanhã é maior do que o de hoje

# In[60]:


ibvsp['Target'] = (ibvsp['Tomorrow'] > ibvsp['Close']).astype(int)


# In[61]:


ibvsp


# Para conseguirmos ter uma análise mais precisa do mercado, utilizaremos dados a partir de 1990, para evitarmos diferenças de fundamentações do mercado. 

# In[62]:


ibvsp = ibvsp.loc['1990-01-01 00:00:00-03:00':].copy()


# In[63]:


ibvsp


# **4º - Treinando um modelo inicial de Machine Learning**

# Utilizaremos o algoritmo de Random Forest para nosso modelo inicial, que no caso que ele vai treinar várias árvores de decisões individuais, com parâmetros aleatórios e calculando a média dessas árvores de decisões. Por causa disso o Random Foreset é dificil de ter Overfitting e esse algoritmo será bom, porque roda mais rápido e conseguem capturar tendências não lineares  

# In[64]:


from sklearn.ensemble import RandomForestClassifier

#Iniciando nosso modelo
#n_estimators = nº de árvores de decisão individual que iremos treinar
#min_samples_split = para evitar overfitting
model = RandomForestClassifier(n_estimators=100, min_samples_split=100)


# **OBS: ESSES DADOS SÃO DE SÉRIES TEMPORAIS, E COM DADOS DE SÉRIES TEMPORAIS VOCÊ NÃO PODE USAR 'VALIDAÇÃO CRUZADA (CROSS VALIDATION)',PORQUE SEUS RESULTADOS DE TREINO PODEM ATÉ FICAR BONS, MAS SEUS RESULTADOS REAIS FICARÃO HORRÍVEIS!!**

# Iremos separar nossos dados em dados de treino e teste.

# In[66]:


train = ibvsp.iloc[:-100]
test = ibvsp.iloc[-100:]


# In[68]:


predictors = ['Close','Volume','Open','High','Low']
model.fit(train[predictors], train['Target'])


# Agora vamos medir quão preciso é o modelo. Iremos medir se o modelo está fazendo o que estamos querendo ou não.

# In[70]:


from sklearn.metrics import precision_score

preds = model.predict(test[predictors])


# In[72]:


import pandas as pd
preds = pd.Series(preds, index=test.index)


# In[73]:


preds


# In[74]:


precision_score(test['Target'], preds)


# Verificamos que nossa pontuação de precisão não é muito boa, então quando dizemos que o preço das ações subiria, ele subiu apenas 48% das vezes, o que não é muito bom.

# In[77]:


combined = pd.concat([test['Target'],preds], axis=1)


# Para podermos visualizar melhor nossas previsões comparados com o que aconteceu de fato, veremos no gráfico

# In[79]:


combined.plot()


# **5º - Construindo um sistema de backtesting**

# Agora construiremos uma forma mais robusta de testar nosso algoritmo. Iremos testar ao invés dos útlimos 100 dias, veremos como nosso modelo lida com dados dos últimos anos, para ter como noção muitas situações diferentes.Para isso iremos utilizar o princípio de **backtesting** que é um teste que ajuda a identificar padrões ou comportamentos que podem ser percebidos a partir de dados do passado.

# In[80]:


def predict(train, test, prediction, model):
    model.fit(train[predictors], train['Target'])
    preds = model.predict(test[predictors])
    preds = pd.Series(preds, index=test.index, name='Predictions')
    combined = pd.concat([test['Target'],preds], axis=1)
    return combined


# In[81]:


def backtest(data, model, predictors, start=2500, step=250):
    all_predictions = []
    
    for i in range(start, data.shape[0], step):
        train = data.iloc[0:i].copy()
        test = data.iloc[i:(i + step)].copy()
        predictions= predict(train, test, predictors, model)
        all_predictions.append(predictions)
    return pd.concat(all_predictions)    
    


# In[82]:


predictions = backtest(ibvsp, model,predictors)


# In[83]:


predictions['Predictions'].value_counts()


# Nós prevemos que o mercado cairia em cerca de 2654 vezes e subiria 2600 vezes

# In[86]:


precision_score(predictions['Target'], predictions['Predictions'])


# Concluímos que em cerca de 5200 dias tivemos uma precisão de 51% de acurácia.

# In[87]:


predictions['Target'].value_counts()/ predictions.shape[0]


# A IBOVESPA nos dias que estávamos analisando aumentou 52,18% dos dias e caiu 47,81% dos dias,o algoritmo teve um desempenho um pouco pior que a apenas a procentagem natural de dias.

# **6º - Adicionando preditores adicionais no nosso modelo**

# In[91]:


# Calcular o preço médio de fechamentos nesses horizontes
horizons = [2,5,60,250,1000]
new_predictors = []

# Criamos um loop por esses horizontes para calcular a média móvel
for horizon in horizons:
    rolling_averages = ibvsp.rolling(horizon).mean()
    
    # Adicionaremos uma coluna da razão entre o fechamento e a média móvel do fechamento no horizonte
    ration_column = f'Close Ratio {horizon}'
    ibvsp[ration_column] = ibvsp['Close']/ rolling_averages['Close']
    
    # Adcionaremos uma coluna de tendências desses horizontes para verificar quando o preço das ações realmente subiu
    trend_column = f'Trend_{horizon}'
    ibvsp[trend_column] = ibvsp.shift(1).rolling(horizon).sum()['Target']
    
    new_predictors += [ration_column, trend_column]


# Iremos calcular o preço médio de fechamentos nesses horizonte para encontrar uma relação entre o preço de fechamento de hoje e o preço de fechamento nesses horizontes, e vermos por exemplo se subiu muito pode ser uma desaceleração, se o mercado caiu muito, pode ser uma recuperação,
# 

# In[94]:


ibvsp = ibvsp.dropna()


# In[95]:


ibvsp


# **7º - Aprimorando nosso modelo**

# In[96]:


#Mudamos nosso min_samples_split e nosso n_estimators
model = RandomForestClassifier(n_estimators=200, min_samples_split=50, random_state=1)


# In[97]:


def predict(train, test, prediction, model):
    model.fit(train[predictors], train['Target'])
    # medir a probabilidade que a ação irá subir amanhã
    preds = model.predict_proba(test[predictors])[:,1]
    #se o a previsão for de acima de 60% que ela irá subir 
    preds[preds >= .6] = 1
    #se o a previsão for de abaixo de 60% que ela irá subir 
    preds[preds< .6] = 0
    preds = pd.Series(preds, index=test.index, name='Predictions')
    combined = pd.concat([test['Target'],preds], axis=1)
    return combined


# In[98]:


predictions = backtest(ibvsp, model, new_predictors)


# In[99]:


predictions['Predictions'].value_counts()


# In[100]:


precision_score(predictions['Target'], predictions['Predictions'])


# # Conclusão

# O nosso modelo obteve uma acurácia de que as ações subiriam de 50,98%, ainda não é um resultado que nos traz uma certeza de que ação irá subir, mas isso pode vir a ocorrer devidos à fatores externos que não podemos analisar neste dataset, como outros índices ao redor do mundo que possa ter alguma correlação com a IBOVESPA, algumas notícias e condições macroeconômicas gerais, como taxas de juros, inflação, podem vir a influenciar também, entre outros fatores que podem vir a influenciar e não estão presentes neste dataset.
