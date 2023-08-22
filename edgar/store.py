import pandas as pd
from edgar.report import fundamentals


def save_to_csv(symbol: str, df: pd.DataFrame, path: str = None):
    if path == None:
        path = "../data/" + symbol.lower() + ".csv"
    df.to_csv(path, index=False)


def load_from_csv(symbol: str) -> pd.DataFrame:
    path = "../data/" + symbol.lower() + ".csv"
    return pd.read_csv(path)


def show(tickers: list):
    for ticker in tickers:
        print(ticker)
        df = load_from_csv(ticker)
        fd = fundamentals(ticker, df)
        print(fd.format())
