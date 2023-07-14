# General
CONTEXT_REFERENCE1 = "contextref"
CONTEXT_REFERENCE2 = "contextRef"

# Stock Information
DEI_STOCKCOUNT = "dei:EntityCommonStockSharesOutstanding"
DEI_FILINGDATE = "dei:DocumentPeriodEndDate"

# Income Statement
USGAAP_REVENUE1 = "us-gaap:revenues".lower()
USGAAP_REVENUE2 = "us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax".lower()
USGAAP_REVENUE3 = "us-gaap:SalesRevenueNet".lower()
USGAAP_GROSSPROFIT = "us-gaap:grossprofit".lower()
USGAAP_NETINCOME1 = "us-gaap:netincomeloss".lower()
USGAAP_NETINCOME2 = "us-gaap:ProfitLoss".lower()
USGAAP_INTERESTEXPENSE = "us-gaap:interestexpense".lower()
USGAAP_OPINCOME1 = "us-gaap:OperatingIncomeLoss".lower()
USGAAP_OPINCOME2 = "us-gaap:IncomeLossFromContinuingOperationsIncludingPortionAttributableToNoncontrollingInterest".lower()
USGAAP_OPINCOME3 = "us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest".lower()
USGAAP_COSTOFREV = "us-gaap:CostOfGoodsAndServicesSold".lower()

# Balance Sheet
USGAAP_STOCKHOLDERSEQUITY = "us-gaap:stockholdersequity".lower()
USGAAP_LONGDEBT = "us-gaap:LongTermDebtNoncurrent".lower()
USGAAP_LONGLEASE = "us-gaap:OperatingLeaseLiabilityNoncurrent".lower()
USGAAP_SHORTDEBT = "us-gaap:DebtCurrent".lower()
USGAAP_CASH = "us-gaap:CashAndCashEquivalentsAtCarryingValue".lower()
USGAAP_SECURITIES = "us-gaap:MarketableSecuritiesCurrent".lower()
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
USGAAP_DIVIDEND1 = "us-gaap:paymentsofdividendscommonstock".lower()
USGAAP_DIVIDEND2 = "us-gaap:PaymentsOfDividends".lower()
USGAAP_CAPEX1 = "us-gaap:PaymentsToAcquireProductiveAssets".lower()
USGAAP_CAPEX2 = "us-gaap:PaymentsToAcquirePropertyPlantAndEquipment".lower()
