from portVision.portfolio.returns import stock
from portVision.handler import datahandler

def build_portfolio(universe):
    df = datahandler.get_closes(universe)
    extended_db = stock(df)
    port = extended_db[[col for col in extended_db.columns if "returns" in col]]
    return port