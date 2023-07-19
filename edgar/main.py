import sys
import warnings
from edgar.fetcher import *
from edgar.report import *

warnings.filterwarnings("ignore")
num_params = len(sys.argv)
years = None
if num_params > 1:
    ticker = sys.argv[1]
else:
    sys.exit("no ticker provided for data collection")

if num_params > 2:
    # collect the years to filter
    years = []
    for i in range(2, num_params):
        years.append(sys.argv[i])
print(ticker, years)
xbrlFiles = fetch(ticker, years)
df = fundamentals(ticker)
for yy, doc in xbrlFiles.items():
    p = xbrlParser(doc)
    df.insert(p)
df.print()
