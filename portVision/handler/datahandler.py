from typing import List, TypeVar
import pandas_datareader as web
import pandas as pd 

DF = TypeVar('DF')

def get_volume(tickers:List) -> DF:
    pass 

def get_ohlc(tickers:List) -> DF:
    pass 

def get_close(tickers) -> DF:
    data = web.get_data_yahoo(tickers)
    return data['Adj Close']


