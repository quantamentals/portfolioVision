import numpy as np
from scipy.stats import linregress
from portVision.handler import datahandler


"""Single stock related"""

def daily_vol(df):
    return (df['Adj Close'] / df['Adj Close'].shift(1)).std()

def annual_vol(df):
    return daily_vol(df) * np.sqrt(250)

def daily_log_vol(df):
    return np.log(df['Adj Close'] / df['Adj Close'].shift(1)).std()

def annual_log_vol(df):
    return daily_log_vol(df) * np.sqrt(250)

"""Portfolio Related """

def asset_vol(port,ticker, annualized=True):
    daily_vol = port[ticker].std()
    if annualized == True:
        return daily_vol * np.sqrt(250)
    return daily_vol


def asset_beta(ticker):
    inputs = datahandler.get_closes([ticker,'^GSPC'])
    rets = inputs.pct_change().dropna()
    return linregress(y=rets[ticker], x=rets['^GSPC'])[0]



def portfolio_risk():
    pass 


def portfolio_risk_contribs():
    pass 


