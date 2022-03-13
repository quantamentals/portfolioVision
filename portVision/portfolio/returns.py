import pandas_datareader as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
plt.style.use('seaborn')


def stock(prices_df): #change to just stock
    df = prices_df.copy()
    cols = df.columns
    for symbol in cols:
        df[f"{symbol} returns"] = df[symbol].pct_change()
    df.dropna(inplace=True)
    return df


def portfolio(prices_df): # change to just portfolio
    rets = stock(prices_df)
    return rets[[asset for asset in rets.columns if 'returns' in asset]]


def getExpectedReturn(port_rets,ticker,annualised=True):
    """ This is the mean historical return either daily or annualized"""

    daily_returns = port_rets[f'{ticker} returns']

    expected_return_daily = daily_returns.mean()

    if annualised:
        expected_return_annual = ((1+expected_return_daily)**250)-1
        
        return expected_return_annual
        
    return expected_return_daily