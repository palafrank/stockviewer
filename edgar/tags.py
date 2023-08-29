# General
CONTEXT_REFERENCE1 = "contextref"
CONTEXT_REFERENCE2 = "contextRef"

# Stock Information
DEI_STOCKCOUNT = "dei:EntityCommonStockSharesOutstanding".lower()
DEI_FILINGDATE = "dei:DocumentPeriodEndDate"

# Income Statement
USGAAP_REVENUE1 = "us-gaap:revenues".lower()
USGAAP_REVENUE2 = "us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax".lower()
USGAAP_REVENUE3 = "us-gaap:SalesRevenueNet".lower()
USGAAP_GROSSPROFIT = "us-gaap:grossprofit".lower()

# Net Income
USGAAP_NETINCOME1 = "us-gaap:netincomeloss".lower()
USGAAP_NETINCOME2 = "us-gaap:ProfitLoss".lower()
USGAAP_NETINCOME3 = "us-gaap:NetIncomeLossAvailableToCommonStockholdersBasic".lower()
USGAAP_NETINCOME = [USGAAP_NETINCOME1, USGAAP_NETINCOME2, USGAAP_NETINCOME3]

USGAAP_INTERESTEXPENSE1 = "us-gaap:interestexpense".lower()
USGAAP_INTERESTEXPENSE2 = "us-gaap:InterestPaidNet".lower()
USGAAP_INTERESTEXPENSE3 = "us-gaap:InterestExpenseDebt".lower()
USGAAP_INTERESTEXPENSE = [
    USGAAP_INTERESTEXPENSE1,
    USGAAP_INTERESTEXPENSE2,
    USGAAP_INTERESTEXPENSE3,
]
USGAAP_OPINCOME1 = "us-gaap:OperatingIncomeLoss".lower()
USGAAP_OPINCOME2 = "us-gaap:IncomeLossFromContinuingOperationsIncludingPortionAttributableToNoncontrollingInterest".lower()
USGAAP_OPINCOME3 = "us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest".lower()
USGAAP_COSTOFREV = "us-gaap:CostOfGoodsAndServicesSold".lower()

# Balance Sheet
USGAAP_STOCKHOLDERSEQUITY1 = "us-gaap:stockholdersequity".lower()
USGAAP_STOCKHOLDERSEQUITY2 = "us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest".lower()
USGAAP_STOCKHOLDERSEQUITY = [USGAAP_STOCKHOLDERSEQUITY1, USGAAP_STOCKHOLDERSEQUITY2]

USGAAP_LONGDEBT1 = "us-gaap:LongTermDebtNoncurrent".lower()
USGAAP_LONGDEBT2 = "us-gaap:LongTermDebtAndCapitalLeaseObligations".lower()
USGAAP_LONGDEBT = [USGAAP_LONGDEBT1, USGAAP_LONGDEBT2]
USGAAP_LONGLEASE = "us-gaap:OperatingLeaseLiabilityNoncurrent".lower()
USGAAP_SHORTDEBT1 = "us-gaap:DebtCurrent".lower()
USGAAP_SHORTDEBT2 = "us-gaap:LongTermDebtCurrent".lower()
USGAAP_SHORTDEBT = [USGAAP_SHORTDEBT1, USGAAP_SHORTDEBT2]

# Cash And Equivalents
USGAAP_CASH1 = "us-gaap:CashAndCashEquivalentsAtCarryingValue".lower()
USGAAP_CASH2 = "us-gaap:CashCashEquivalentsAndShortTermInvestments".lower()
USGAAP_SECURITIES1 = "us-gaap:MarketableSecuritiesCurrent".lower()
USGAAP_SECURITIES2 = "us-gaap:ShortTermInvestments".lower()
USGAAP_CASH = [USGAAP_CASH1, USGAAP_CASH2]
USGAAP_SECURITIES = [USGAAP_SECURITIES1, USGAAP_SECURITIES2]

USGAAP_CURRENTASSETS = "us-gaap:AssetsCurrent".lower()
USGAAP_CURRENTLIABILITES = "us-gaap:LiabilitiesCurrent".lower()
USGAAP_RETAINEDEARNINGS = "us-gaap:RetainedEarningsAccumulatedDeficit".lower()
USGAAP_GOODWILL = "us-gaap:Goodwill".lower()
USGAAP_INTANGIBLE = "us-gaap:IntangibleAssetsNetExcludingGoodwil".lower()

# CashFlow Statement
USGAAP_OPCASHFLOW1 = "us-gaap:netcashprovidedbyusedinoperatingactivities".lower()
USGAAP_OPCASHFLOW2 = (
    "us-gaap:NetCashProvidedByUsedInOperatingActivitiesContinuingOperations".lower()
)
USGAAP_OPCASHFLOW = [USGAAP_OPCASHFLOW1, USGAAP_OPCASHFLOW2]

USGAAP_DIVIDEND1 = "us-gaap:paymentsofdividendscommonstock".lower()
USGAAP_DIVIDEND2 = "us-gaap:PaymentsOfDividends".lower()
USGAAP_DIVIDEND3 = "us-gaap:PaymentsToMinorityShareholders".lower()
USGAAP_DIVIDEND = [USGAAP_DIVIDEND1, USGAAP_DIVIDEND2, USGAAP_DIVIDEND3]

# Capex
USGAAP_CAPEX1 = "us-gaap:PaymentsToAcquireProductiveAssets".lower()
USGAAP_CAPEX2 = "us-gaap:PaymentsToAcquirePropertyPlantAndEquipment".lower()
USGAAP_CAPEX3 = "us-gaap:PaymentsToAcquireOtherProductiveAssets".lower()
USGAAP_CAPEX = [USGAAP_CAPEX1, USGAAP_CAPEX2, USGAAP_CAPEX3]
