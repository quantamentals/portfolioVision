from typing import List, TypeVar, AnyStr
import pandas_datareader as web
import pandas as pd 
import yfinance as yf

DF = TypeVar('DF')

def get_volume(tickers:List) -> DF:
    pass 

def get_ohlc(ticker:AnyStr) -> DF:
    return web.get_data_yahoo(ticker)

def get_close(ticker) -> DF:
    return get_ohlc(ticker)['Adj Close']

def get_ohlcs(tickers:List) -> DF:
    data = {}
    for ticker in tickers:
        data[ticker] = web.get_data_yahoo(ticker) # multi thread this call
    df = pd.concat(data, axis=1)
    return df
    

def get_closes(tickers) -> DF:
    """Update to handle start and end date and default if no params"""
    data = {}
    for ticker in tickers:
        data[ticker] = web.get_data_yahoo(ticker)['Adj Close'] # multi thread this call
    df = pd.concat(data, axis=1)
    return df

