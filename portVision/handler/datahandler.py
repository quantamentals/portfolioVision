from typing import List, TypeVar
import pandas_datareader as web
import pandas as pd 

DF = TypeVar('DF')

def get_volume(tickers:List) -> DF:
    pass 

def get_ohlc(tickers:List) -> DF:
    pass 

def get_close(tickers) -> DF:
    """Update to handle start and end date and default if no params"""
    data = {}
    for ticker in tickers:
        data[ticker] = web.get_data_yahoo(ticker)['Adj Close'] # multi thread this call
    df = pd.concat(data, axis=1)
    return df

