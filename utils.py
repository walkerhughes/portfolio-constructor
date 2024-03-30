# helper functions to use in app.py

import yfinance as yf 

def get_checkbox_column_labels(): 
    return [
        ["XLC (Comms)", "XLF (Financials)", "XLRE (Real Estate)"],  
        ["XLY (Consumer)", "XLV (Healthcare)", "XLK (Technology)"],  
        ["XLE (Energy)", "XLI (Industrials)", "XLU (Utilities)"],  
        ["XLP (Consumer Staples)", "XLB (Materials)", ""]   
    ]

def get_sector_etf_tickers(): 
    return ["XLC", "XLF", "XLRE", "XLY", "XLV", "XLK", "XLE", "XLI", "XLU", "XLP", "XLB"]


def get_ticker_data(ticker, start, end):
    pass 