#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:27:55 2020

@author: sage

Yfinance: biblioteca em Python que faz requisições para API do Yahoo Finance

Métodos:
    -> download (DataFrame em pandas):
            Dicionário: um conjunto de dados no formato (chave, valor)
    -> Ticker (retornar todas as informações)
            -> dados fundamentalistas
            -> balanço das empresas (anual, trimestral)
"""

import yfinance as yf

stocks = yf.download('ITUB3.SA BBAS3.SA BBDC3.SA',
                     period='1d', interval='1m')

# Acessar um item do dicionário: <nome_do_variavel>[<nome_da_chave>]
#stocks['Close']['BBDC3.SA'].plot()

bradesco_intraday = stocks['Close']['BBDC3.SA']
bradesco_intraday.plot()
