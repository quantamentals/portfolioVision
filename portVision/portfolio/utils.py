from portVision.portfolio.returns import stock_returns 

def build_portfolio(df):
    extended_db = stock_returns(df)
    port = extended_db[[col for col in extended_db.columns if "returns" in col]]
    return port