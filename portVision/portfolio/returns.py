import pandas_datareader as web

def stock_returns(prices_df): #change to just stock
    cols = prices_df.columns
    for symbol in cols:
        prices_df[f"{symbol} returns"] = prices_df[symbol].pct_change()
    prices_df.dropna()
    return prices_df


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




    

