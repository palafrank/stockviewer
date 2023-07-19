import pandas as pd
import numpy as np
import yahoofinance


class fundamentals:
    cols = [
        "Filing",
        "Revenue",
        "Operating Income",
        "Interest",
        "Net Income",
        "Equity",
        "Cash",
        "Debt",
        "Current-Debt",
        "Intangibles",
        "Current-Ratio",
        "Operating CF",
        "Capital Expense",
        "Dividend",
    ]

    def __init__(self, ticker):
        self.data = pd.DataFrame(
            columns=self.cols,
        )
        self.price = yahoofinance.price(ticker)

    def insert(self, parser):
        self.data.loc[len(self.data)] = {
            self.cols[0]: parser.filingDate,
            self.cols[1]: parser.gaap.revenue(),
            self.cols[2]: parser.gaap.op_income(),
            self.cols[3]: parser.gaap.interest_expense(),
            self.cols[4]: parser.gaap.net_income(),
            self.cols[5]: parser.gaap.equity(),
            self.cols[6]: parser.gaap.cash(),
            self.cols[7]: parser.gaap.debt(),
            self.cols[8]: parser.gaap.debt(True),
            self.cols[9]: parser.gaap.intangibles(),
            self.cols[10]: parser.gaap.current_ratio(),
            self.cols[11]: parser.gaap.operating_cf(),
            self.cols[12]: parser.gaap.capex(),
            self.cols[13]: parser.gaap.dividend(),
        }
    
    def generateReport(self):
        self.insights = dict()
        

    def print(self):
        print(self.data)
