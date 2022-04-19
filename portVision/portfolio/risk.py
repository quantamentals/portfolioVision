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
def cov_matrix_daily(ret_df):
    return ret_df.cov()

def cov_matrix_annual(ret_df):
    return cov_matrix_daily(ret_df=ret_df)*250

def corr_matrix(ret_df):
    return ret_df.corr()

def asset_vol(port,ticker, annualized=True):
    daily_vol = port[ticker].std()
    if annualized == True:
        return daily_vol * np.sqrt(250)
    return daily_vol

def asset_beta(ticker):
    inputs = datahandler.get_closes([ticker,'^GSPC'])
    rets = inputs.pct_change().dropna()
    return linregress(y=rets[ticker], x=rets['^GSPC'])[0]

def portfolio_var(ret_df, weights):
    w = np.array(weights)
    # w ∑ w 
    return np.dot(w.T, np.dot(ret_df.cov() * 250, w))

def portfolio_vol(ret_df, weights):
    return np.sqrt(portfolio_var(ret_df,weights))


