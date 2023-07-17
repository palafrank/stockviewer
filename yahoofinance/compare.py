import yfinance as yf
import pandas as pd
import sys

TICKER = "symbol"
# Fundamentals
# Income
MARKETCAP = "marketCap"
REVENUE = "totalRevenue"
GROSS = "grossProfits"
EBITDA = "ebitda"
NET_INCOME = "netIncomeToCommon"

# Assets
CASH = "totalCash"
CURRENT_RATIO = "currentRatio"
DEBT = "totalDebt"
DEBT_TO_EQUITY = "debtToEquity"

# Cash Flow
FCF = "freeCashflow"
OP_CF = "operatingCashflow"
PAYOUT_RATIO = "payoutRatio"

# Metrics
GROSS_MARGIN = "grossMargins"
OP_MARGIN = "operatingMargins"
REV_GROWTH = "revenueGrowth"
EARNING_GROWTH = "earningsGrowth"

# Returns
ROA = "returnOnAssets"
ROE = "returnOnEquity"
TRAILING_PE = "trailingPE"
FORWARD_PE = "forwardPE"


class comparator:
    cols = [
        TICKER,
        MARKETCAP,
        REVENUE,
        GROSS,
        EBITDA,
        NET_INCOME,
        CASH,
        CURRENT_RATIO,
        DEBT,
        DEBT_TO_EQUITY,
        FCF,
        OP_CF,
        PAYOUT_RATIO,
        GROSS_MARGIN,
        OP_MARGIN,
        REV_GROWTH,
        EARNING_GROWTH,
        ROA,
        ROE,
        TRAILING_PE,
        FORWARD_PE,
    ]

    def __init__(self, tickers):
        self.data = pd.DataFrame(
            columns=self.cols,
        )
        for ticker in tickers:
            info = yf.Ticker(ticker)
            loc = len(self.data)
            for item in self.cols:
                try:
                    self.data.at[loc, item] = info.info[item]
                except:
                    self.data.at[loc, item] = "--"

    def info(self):
        return self.data

