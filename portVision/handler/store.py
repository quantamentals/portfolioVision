import sqlite3
import pandas as pd
from portVision.handler import datahandler

def write_prices(df):
    conn = sqlite3.connect("universeDB")
    df.to_sql('adjclose',conn,if_exists="replace")
    conn.close()

def append_prices(df):
    conn = sqlite3.connect("universeDB")
    existing = read_prices()
    for col in df.columns:
        existing[col]= df[col]
    existing.to_sql('adjclose',conn,if_exists="replace")
    conn.close()

def read_prices():
    conn = sqlite3.connect("universeDB")
    sql = """ SELECT * from adjclose"""
    df = pd.read_sql(sql,conn,index_col="Date")
    return df

def build_universe(symbols_list):
    df = datahandler.get_close(symbols_list)
    write_prices(df)
    return df

def append_universe(symbols_list):
     df = datahandler.get_close(symbols_list)
     append_prices(df)
     return df