#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat May 9 18:14:19 2020

@author: sage

Coletar os dados históricos dos principais índices acionários globais e 
analisar seu desempenho durante a crise do coronavírus
"""

import yfinance as yf
import pandas as pd

# S&P500, Nikkei, FTSE, IBOV
indices_list = ['^GSPC', '^N225', '^FTSE', '^BVSP']

# Fazer o download dos dados históricos dos índices
# Referência: 04/03/2020 - 08/05/2020
indices_df = yf.download(indices_list, 
                         start='2020-03-04', 
                         end='2020-05-08')['Close']

# Realizar a análise de variação em porcentagem
indices_pct = pd.DataFrame()

for col in indices_df.columns: # Transformar cada uma das colunas
    indices_pct[col] = (indices_df[col] / indices_df[col].iloc[0]) - 1

indices_pct.interpolate(method='linear').plot()

# Valores médios (média de cada coluna)
mean = indices_df.mean()

# Desvio Padrão
desv_pad = indices_df.std()

# Correlação (retorna uma nxn)
correl = indices_df.corr()