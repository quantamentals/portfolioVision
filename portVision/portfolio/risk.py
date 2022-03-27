import numpy as np
from scipy.stats import linregress
from portVision.handler import datahandler

def vol(port,ticker, annualized=True):
    daily_vol = port[ticker].std()
    if annualized == True:
        return daily_vol * np.sqrt(250)
    return daily_vol


def beta(ticker):
    inputs = datahandler.get_closes([ticker,'^GSPC'])
    rets = inputs.pct_change().dropna()
    return linregress(y=rets[ticker], x=rets['^GSPC'])[0]



