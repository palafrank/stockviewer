from edgar.tags import *
import numpy


class gaapDB:
    def __init__(self, data):
        self.data = data

    def int64(self, data) -> numpy.int64:
        splits = data.split(".")
        return numpy.int64(splits[0])

    def revenue(self):
        if USGAAP_REVENUE1 in self.data:
            return self.data[USGAAP_REVENUE1]
        if USGAAP_REVENUE2 in self.data:
            return self.data[USGAAP_REVENUE2]
        if USGAAP_REVENUE3 in self.data:
            return self.data[USGAAP_REVENUE3]
        else:
            return "--"

    def equity(self):
        if USGAAP_STOCKHOLDERSEQUITY in self.data:
            return self.data[USGAAP_STOCKHOLDERSEQUITY]
        else:
            return "--"

    def debt(self, current=False):
        total = 0
        if current and USGAAP_SHORTDEBT in self.data:
            return str(self.int64(self.data[USGAAP_SHORTDEBT]))
        if USGAAP_LONGDEBT in self.data:
            total = total + self.int64(self.data[USGAAP_LONGDEBT])
        if USGAAP_SHORTDEBT in self.data:
            total = total + self.int64(self.data[USGAAP_SHORTDEBT])
        if USGAAP_LONGLEASE in self.data:
            total = total + self.int64(self.data[USGAAP_LONGLEASE])
        return str(total)

    def op_income(self):
        if USGAAP_OPINCOME1 in self.data:
            return self.data[USGAAP_OPINCOME1]
        elif USGAAP_OPINCOME2 in self.data:
            return self.data[USGAAP_OPINCOME2]
        elif USGAAP_OPINCOME3 in self.data:
            return self.data[USGAAP_OPINCOME3]
        else:
            return "--"

    def current_ratio(self):
        if USGAAP_CURRENTASSETS in self.data and USGAAP_CURRENTLIABILITES in self.data:
            ca = self.int64(self.data[USGAAP_CURRENTASSETS])
            cl = self.int64(self.data[USGAAP_CURRENTLIABILITES])
            return str(round(ca / cl, 2))
        else:
            return "--"

    def cash(self):
        total = 0
        if USGAAP_CASH in self.data:
            total = self.int64(self.data[USGAAP_CASH])
        if USGAAP_SECURITIES in self.data:
            total = total + self.int64(self.data[USGAAP_SECURITIES])
        return str(total)

    def intangibles(self):
        total = 0
        if USGAAP_GOODWILL in self.data or USGAAP_INTANGIBLE in self.data:
            if USGAAP_GOODWILL in self.data:
                total = total + self.int64(self.data[USGAAP_GOODWILL])
            if USGAAP_INTANGIBLE in self.data:
                total = total + self.int64(self.data[USGAAP_INTANGIBLE])
            return str(total)
        else:
            return "--"

    def interest_expense(self):
        if USGAAP_INTERESTEXPENSE in self.data:
            return self.data[USGAAP_INTERESTEXPENSE]
        else:
            return "--"

    def net_income(self):
        if USGAAP_NETINCOME1 in self.data:
            return self.data[USGAAP_NETINCOME1]
        if USGAAP_NETINCOME2 in self.data:
            return self.data[USGAAP_NETINCOME2]
        else:
            return "--"

    def operating_cf(self):
        if USGAAP_OPCASHFLOW1 in self.data:
            return self.data[USGAAP_OPCASHFLOW1]
        if USGAAP_OPCASHFLOW2 in self.data:
            return self.data[USGAAP_OPCASHFLOW2]
        return "--"

    def capex(self):
        if USGAAP_CAPEX1 in self.data:
            return self.data[USGAAP_CAPEX1]
        if USGAAP_CAPEX2 in self.data:
            return self.data[USGAAP_CAPEX2]
        return "--"

    def dividend(self):
        if USGAAP_DIVIDEND1 in self.data:
            return self.data[USGAAP_DIVIDEND1]
        elif USGAAP_DIVIDEND2 in self.data:
            return self.data[USGAAP_DIVIDEND2]
        else:
            return "--"
