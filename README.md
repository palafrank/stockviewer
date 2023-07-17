# Stock Viewer

### /yahoofinance
Tool to quickly compare fundamental metrics of multiple tickers using information pulled from Yahoo finance

### /edgar
Tool to pull historic filing data from edgar XBRL filings

### Examples

```
cd yahoofinance
python compare_main.py HPQ DELL HPE
  symbol    marketCap totalRevenue grossProfits      ebitda netIncomeToCommon   totalCash currentRatio    totalDebt  ... payoutRatio grossMargins operatingMargins revenueGrowth earningsGrowth returnOnAssets returnOnEquity trailingPE forwardPE
0    HPQ  32980228096  56206000128  12335000000  5200000000        2670000128  1940000000        0.708  11992999936  ...      0.3839      0.20202          0.07809        -0.217          0.138        0.07193             --   12.52809  9.396068
1   DELL  40536526848  97107001344  22686000000  7408999936        1952999936  7836000256        0.799  29365999616  ...      0.5113      0.22573          0.05448        -0.199         -0.423        0.03833             --  20.954887  9.137706
2    HPE  22382041088  29603999744   9506000000  5098999808        1024000000  1980999936        0.867  13500000256  ...      0.6076      0.33962          0.08627         0.039          0.684        0.02854        0.04995  21.936708  8.136149

[3 rows x 21 columns]
```