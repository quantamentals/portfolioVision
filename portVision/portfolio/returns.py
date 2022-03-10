import pandas_datareader as web
import numpy as np

def stock_returns(prices_df): #change to just stock
    df = prices_df.copy()
    cols = df.columns
    for symbol in cols:
        df[f"{symbol} returns"] = df[symbol].pct_change()
    df.dropna(inplace=True)
    return df


def portfolio_returns(prices_df): # change to just portfolio
    rets = stock_returns(prices_df)
    return rets[[asset for asset in rets.columns if 'returns' in asset]]


def ewp(port_rets):
    no_assets = len(port_rets.columns)
    weights = [1/no_assets for i in range(no_assets)]
    return port_rets.dot(weights)


def ewp_contribs(port_rets):
    no_assets = len(port_rets.columns)
    weights = [1/no_assets for i in range(no_assets)]
    equal_contrib = port_rets.mul(weights, axis="columns")
    equal_contrib['EWP'] = equal_contrib.sum(axis=1)
    return equal_contrib


def _ewp_stats(port_rets):
    contrib = ewp_contribs(port_rets)
    stats = contrib.agg(["mean","std"]).T
    return stats


def ewp_expected(port_rets):
    stats = _ewp_stats(port_rets)
    stats.columns=['er','vol']
    stats['er'] = stats['er'] * 252
    stats['vol'] = stats['vol'] * np.sqrt(252)
    return stats

    

