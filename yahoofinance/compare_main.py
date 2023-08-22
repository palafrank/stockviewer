import sys
from compare import comparator

num_params = len(sys.argv)
if num_params == 1:
    sys.exit("no ticker(s) provided for data collection")
tickers = []
for i in range(1, num_params):
    tickers.append(sys.argv[i])
comp = comparator(tickers)
# with pd.option_context("display.max_rows", None, "display.max_columns", None):
print(comp.info().to_string(index=False))
