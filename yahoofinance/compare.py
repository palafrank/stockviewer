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

# Stock Info
PRICE = "currentPrice"


class comparator:
    cols = [
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
        PRICE,
    ]

    def __init__(self, tickers):
        cols = tickers.copy()
        cols.insert(0, "Metrics")
        self.data = pd.DataFrame(
            columns=cols,
        )
        yinfo = dict()
        for ticker in tickers:
            yinfo[ticker] = yf.Ticker(ticker)
        for index in self.cols:
            row = []
            row.append(index)
            for ticker in tickers:
                try:
                    num = yinfo[ticker].info[index]
                    row.append("{:,.2f}".format(float(num)))
                except:
                    row.append("--")
            self.data.loc[len(self.data)] = row

    def info(self):
        return self.data
