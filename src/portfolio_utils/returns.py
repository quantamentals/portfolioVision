import pandas_datareader as web

def stock_returns(prices_df):
    cols = prices_df.columns
    for symbol in cols:
        prices_df[f"{symbol} returns"] = prices_df[symbol].pct_change()
    return prices_df



