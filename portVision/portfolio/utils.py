from portVision.portfolio.returns import stock_returns 
from portVision.handler import datahandler

def build_portfolio(universe):
    df = datahandler.get_close(universe)
    extended_db = stock_returns(df)
    port = extended_db[[col for col in extended_db.columns if "returns" in col]]
    return port