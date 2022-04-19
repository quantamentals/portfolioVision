from portVision.portfolio.returns import get_stock
from portVision.handler import datahandler

"""

Make all utils functions work from raw tickers and return dataframes, similar to risk and return modules

"""

def build_portfolio(universe:list):
    df = datahandler.get_closes(universe)
    extended_db = get_stock(df)
    port = extended_db[[col for col in extended_db.columns if "returns" in col]]
    return port


def build_indexes():
    markets = ['^GSPC','^IXIC','^DJI', '^RUT','^VIX']
    idxs = build_portfolio(markets)
    return idxs 


def build_futures():
    contracts = ["NG=F","CL=F","GC=F","BZ=F"]
    return build_portfolio(contracts)


def normalized(universe:list):
    dfs = datahandler.get_closes(universe)
    return (dfs / dfs.iloc[0] * 100 ).plot(figsize=(15,6))


def normalized_indexes():
    markets = ['^GSPC','^IXIC','^DJI', '^RUT','^VIX']
    return normalized(markets)


def market_compare(ticker:str):
    markets = ['^GSPC','^IXIC','^DJI', '^RUT','^VIX']
    markets.append(ticker)
    return normalized(markets)


