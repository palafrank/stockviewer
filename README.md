# Stock Viewer

### /yahoofinance
Tool to quickly compare fundamental metrics of multiple tickers using information pulled from Yahoo finance

### /edgar
Tool to pull historic filing data from edgar XBRL filings

### Examples

```
cd yahoofinance
python compare_main.py HPQ DELL HPE
          Metrics               HPQ               HPE              DELL
        marketCap 30,929,438,720.00 21,749,196,800.00 41,089,228,800.00
     totalRevenue 56,206,000,128.00 29,603,999,744.00 97,107,001,344.00
     grossProfits 12,335,000,000.00  9,506,000,000.00 22,686,000,000.00
           ebitda  5,200,000,000.00  5,098,999,808.00  8,211,999,744.00
netIncomeToCommon  2,670,000,128.00  1,024,000,000.00  1,952,999,936.00
        totalCash  1,940,000,000.00  1,980,999,936.00  7,836,000,256.00
     currentRatio              0.71              0.87              0.80
        totalDebt 11,992,999,936.00 13,500,000,256.00 29,365,999,616.00
     debtToEquity                --             66.11                --
     freeCashflow  2,408,124,928.00  1,797,250,048.00  2,320,999,936.00
operatingCashflow  2,918,000,128.00  4,350,000,128.00  5,610,999,808.00
      payoutRatio              0.38              0.61              0.51
     grossMargins              0.20              0.34              0.23
 operatingMargins              0.08              0.09              0.05
    revenueGrowth             -0.22              0.04             -0.20
   earningsGrowth              0.14              0.68             -0.42
   returnOnAssets              0.07              0.03              0.04
   returnOnEquity                --              0.05                --
       trailingPE             11.75             21.32             21.40
        forwardPE              8.81              7.87              9.22
     currentPrice             31.37             16.84             56.50
```

```
cd edgar
python main.py HPQ 2022 2021 2020 2019 2018

HPQ ['2022', '2021', '2020', '2019', '2018']
{'2022': '/Archives/edgar/data/47217/000004721722000068/0000047217-22-000068-index.htm', '2021': '/Archives/edgar/data/47217/000004721721000060/0000047217-21-000060-index.htm', '2020': '/Archives/edgar/data/47217/000004721720000045/0000047217-20-000045-index.htm', '2019': '/Archives/edgar/data/47217/000004721719000071/0000047217-19-000071-index.htm', '2018': '/Archives/edgar/data/47217/000004721718000052/0000047217-18-000052-index.htm'}
--- Filing Data ---
Filed                       2022            2021            2020            2019            2018
Reported                    2022            2021            2020            2019            2018
Revenue           62,983,000,000  63,487,000,000  56,639,000,000  58,756,000,000  58,472,000,000
Operating Income   4,676,000,000   5,302,000,000   3,462,000,000   3,877,000,000   4,064,000,000
Interest             305,000,000     261,000,000     227,000,000     240,000,000     329,000,000
Net Income         3,203,000,000   6,503,000,000   2,844,000,000   3,152,000,000   5,327,000,000
Equity            -2,918,000,000  -1,650,000,000  -2,228,000,000  -1,193,000,000    -639,000,000
Cash               3,145,000,000   4,299,000,000   4,864,000,000   4,537,000,000   5,166,000,000
Debt              11,889,000,000   8,428,000,000   7,121,000,000   5,137,000,000   5,987,000,000
Current-Debt         218,000,000   1,106,000,000     674,000,000     357,000,000   1,463,000,000
Intangibles        8,541,000,000   6,803,000,000   6,380,000,000   6,372,000,000   5,968,000,000
Current-Ratio               0.76            0.76            0.79             0.8            0.85
Operating CF       4,463,000,000   6,409,000,000   4,316,000,000   4,654,000,000   4,528,000,000
Capital Expense      791,000,000     582,000,000     580,000,000     671,000,000     546,000,000
Dividend           1,037,000,000     938,000,000     997,000,000     970,000,000     899,000,000
Working Capital   -6,352,000,000  -6,926,000,000  -5,572,000,000  -5,116,000,000  -3,744,000,000
Excess Cash        2,330,000,000   4,628,000,000   2,512,000,000   2,773,000,000   2,754,000,000
Share Count          982,145,796   1,082,722,559   1,289,636,312   1,453,187,484   1,553,494,507
--- Market Data ---
              Metrics                HPQ
0           marketCap  30,929,438,720.00
1        totalRevenue  56,206,000,128.00
2        grossProfits  12,335,000,000.00
3              ebitda   5,200,000,000.00
4   netIncomeToCommon   2,670,000,128.00
5           totalCash   1,940,000,000.00
6        currentRatio               0.71
7           totalDebt  11,992,999,936.00
8        debtToEquity                 --
9        freeCashflow   2,408,124,928.00
10  operatingCashflow   2,918,000,128.00
11        payoutRatio               0.38
12       grossMargins               0.20
13   operatingMargins               0.08
14      revenueGrowth              -0.22
15     earningsGrowth               0.14
16     returnOnAssets               0.07
17     returnOnEquity                 --
18         trailingPE              11.75
19          forwardPE               8.81
20       currentPrice              31.37

```