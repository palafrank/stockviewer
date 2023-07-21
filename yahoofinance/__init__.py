import yfinance as yf
from yahoofinance.compare import *

class ticker:
    def __init__(self, ticker):
        self.ticker = ticker
        self.info = comparator([ticker])

    def print(self):
        print(self.info.info())

    def price(self):
        return self.info.info[PRICE]
    
    def mktcap(self):
        return self.info.info[MARKETCAP]

