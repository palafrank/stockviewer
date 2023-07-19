import yfinance as yf
from yahoofinance.compare import PRICE

def price(ticker):
    info = yf.Ticker(ticker)
    return info.info[PRICE]
