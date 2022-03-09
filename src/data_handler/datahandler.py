import pandas_datareader as web
import pandas as pd 


def get_close(tickers):
    data = web.get_data_yahoo(tickers)
    return data['Adj Close']


