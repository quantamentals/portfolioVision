from email import utils
import pandas_datareader as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
plt.style.use('seaborn')
from portVision.handler import datahandler 


def calc_simple(df):
    # use a conditional to check for Adj Close, Close or price to make dynamic
    return (df['Adj Close'] / df['Adj Close'].shift(1)) - 1 

def calc_avg_daily(df):
    return calc_simple(df).mean()

def calc_avg_annual(df):
    return calc_avg_daily(df) * 250

def calc_log(df):
    return np.log(df['Adj Close'] / df['Adj Close'].shift(1))

def calc_avg_log_daily(df):
    return calc_log(df).mean()

def calc_avg_log_annual(df):
    return calc_avg_log_daily(df) * 250

def display_simple(df):
    # create option for plotly or matplotlib
    return calc_simple(df).plot(figsize=(8,5))

def display_log(df):
    return calc_log(df).plot(figsize=(8,5))

def stock(prices_df): #change to just stock
    """Calculate returns on a collection of close prices accross tickers"""
    df = prices_df.copy()
    cols = df.columns
    for symbol in cols:
        df[f"{symbol} returns"] = df[symbol].pct_change()
    df.dropna(inplace=True)
    return df

def portfolio(prices_df):
    """ Filter stock prices and returns for only returns"""
    rets = stock(prices_df)
    return rets[[asset for asset in rets.columns if 'returns' in asset]]

def expected(port_rets,ticker,annualised=True):
    """ This is the mean historical return either daily or annualized"""

    daily_returns = port_rets[f'{ticker} returns']

    expected_return_daily = daily_returns.mean()

    if annualised:
        return ((1+expected_return_daily)**250)-1
        
    return expected_return_daily

def benchmarks(index:str="^GSPC",rf:str="TLT"):
    """Returns the expected value for the market rate and the risk free rate"""
    benchmarks = datahandler.get_closes([index, rf])
    benchmarks_ret = portfolio(benchmarks)
    risk_free = expected(benchmarks_ret,rf, annualised=True)
    Er_market = expected(benchmarks_ret,index,annualised='True')
    return Er_market, risk_free

def capm(rf,beta,market_er):
    return rf+beta*(market_er-rf )

def capm_by_ticker(symbol):
    """ Get benchmarks, rf and calc beta via risk module the return capm"""
    pass 