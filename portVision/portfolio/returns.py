from email import utils
import pandas_datareader as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
plt.style.use('seaborn')
from portVision.handler import datahandler 


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


def expected(port_rets,ticker,annualised=True):
    """ This is the mean historical return either daily or annualized"""

    daily_returns = port_rets[f'{ticker} returns']

    expected_return_daily = daily_returns.mean()

    if annualised:
        expected_return_annual = ((1+expected_return_daily)**250)-1
        
        return expected_return_annual
        
    return expected_return_daily

def benchmarks(index:str="^GSPC",rf:str="TLT"):
    """Returns the expected value for the market rate and the risk free rate"""
    benchmarks = datahandler.get_close([index, rf])
    benchmarks_ret = portfolio(benchmarks)
    rf = getExpectedReturn(benchmarks_ret,rf, annualised=True)
    Er_market = getExpectedReturn(benchmarks_ret,index,annualised='True')
    return Er_market, rf

def capm(rf,beta,market_er):
    return rf+beta*(market_er-rf )

def capm_by_ticker(symbol):
    """ Get benchmarks, rf and calc beta via risk module the return capm"""
    pass 