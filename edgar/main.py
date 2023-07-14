import sys
import warnings
from fetcher import *
from report import *

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
    for i in range(1, num_params):
        print(sys.argv[i])
        years.append(sys.argv[i])
print(years)
xbrlFiles = fetch(ticker, years)
df = fundamentals()
for yy, doc in xbrlFiles.items():
    p = xbrlParser(doc)
    df.insert(p)
df.print()
