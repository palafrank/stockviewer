import pandas as pd
import numpy as np
import yahoofinance


class fundamentals:
    cols = [
        "Filed",
        "Reported",
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

    def __init__(self, ticker, df: pd.DataFrame = None):
        if df is not None:
            self.data = df
        else:
            self.data = pd.DataFrame(columns=self.cols)
        self.ticker_info = yahoofinance.ticker(ticker)

    def format(self) -> pd.DataFrame:
        sf = self.data.copy()
        try:
            sf.loc[:, "Revenue"] = sf["Revenue"].map("{:,d}".format)
        except:
            pass
        try:
            sf.loc[:, "Operating Income"] = sf["Operating Income"].map("{:,d}".format)
        except:
            pass
        try:
            sf.loc[:, "Interest"] = sf["Interest"].map("{:,d}".format)
        except:
            pass
        try:
            sf.loc[:, "Net Income"] = sf["Net Income"].map("{:,d}".format)
        except:
            pass
        try:
            sf.loc[:, "Equity"] = sf["Equity"].map("{:,d}".format)
        except:
            pass
        try:
            sf.loc[:, "Cash"] = sf["Cash"].map("{:,d}".format)
        except:
            pass
        try:
            sf.loc[:, "Debt"] = sf["Debt"].map("{:,d}".format)
        except:
            pass
        try:
            sf.loc[:, "Current-Debt"] = sf["Current-Debt"].map("{:,d}".format)
        except:
            pass
        try:
            sf.loc[:, "Intangibles"] = sf["Intangibles"].map("{:,d}".format)
        except:
            pass
        try:
            sf.loc[:, "Capital Expense"] = sf["Capital Expense"].map("{:,d}".format)
        except:
            pass
        try:
            sf.loc[:, "Dividend"] = sf["Dividend"].map("{:,d}".format)
        except:
            pass
        return sf

    def insert(self, yy, parser):
        self.data.loc[len(self.data)] = {
            self.cols[0]: yy,
            self.cols[1]: parser.filingDate,
            self.cols[2]: parser.gaap.revenue(),
            self.cols[3]: parser.gaap.op_income(),
            self.cols[4]: parser.gaap.interest_expense(),
            self.cols[5]: parser.gaap.net_income(),
            self.cols[6]: parser.gaap.equity(),
            self.cols[7]: parser.gaap.cash(),
            self.cols[8]: parser.gaap.debt(),
            self.cols[9]: parser.gaap.debt(True),
            self.cols[10]: parser.gaap.intangibles(),
            self.cols[11]: parser.gaap.current_ratio(),
            self.cols[12]: parser.gaap.operating_cf(),
            self.cols[13]: parser.gaap.capex(),
            self.cols[14]: parser.gaap.dividend(),
        }

    def generateReport(self):
        self.insights = dict()

    def print(self):
        print("--- Filing Data ---")
        print(self.format().T.to_string(header=False))
        print("--- Market Data ---")
        print(self.ticker_info.print())
