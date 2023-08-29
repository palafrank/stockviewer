from edgar.tags import *
import numpy


class gaapDB:
    def __init__(self, data):
        self.data = dict([])
        for key, val in data.items():
            try:
                self.data[key] = self.int64(val)
            except:
                self.data[key] = None

    def int64(self, data) -> numpy.int64:
        splits = data.split(".")
        return numpy.int64(splits[0])

    def normalize(self, data):
        if data is None or data == "--":
            return 0
        else:
            return data

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
        for val in USGAAP_STOCKHOLDERSEQUITY:
            if val in self.data:
                return self.data[val]
        return "--"

    def current_debt(self):
        for val in USGAAP_SHORTDEBT:
            if val in self.data:
                return self.data[val]
        return "--"

    def debt(self):
        total = 0
        for val in USGAAP_LONGDEBT:
            if val in self.data:
                total = total + self.data[val]
                break
        total = total + self.normalize(self.current_debt())
        if USGAAP_LONGLEASE in self.data:
            total = total + self.data[USGAAP_LONGLEASE]
        return total

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
            ca = self.data[USGAAP_CURRENTASSETS]
            cl = self.data[USGAAP_CURRENTLIABILITES]
            return round(ca / cl, 2)
        else:
            return "--"

    def working_capital(self):
        if USGAAP_CURRENTASSETS in self.data and USGAAP_CURRENTLIABILITES in self.data:
            ca = self.data[USGAAP_CURRENTASSETS]
            cl = self.data[USGAAP_CURRENTLIABILITES]
            return ca - cl
        else:
            return "--"

    def cash(self):
        total = 0
        for val in USGAAP_CASH:
            if val in self.data:
                total = total + self.data[val]
        for val in USGAAP_SECURITIES:
            if val in self.data:
                total = total + self.data[val]
        return total

    def intangibles(self):
        total = 0
        if USGAAP_GOODWILL in self.data or USGAAP_INTANGIBLE in self.data:
            if USGAAP_GOODWILL in self.data:
                total = total + self.data[USGAAP_GOODWILL]
            if USGAAP_INTANGIBLE in self.data:
                total = total + self.data[USGAAP_INTANGIBLE]
            return total
        else:
            return "--"

    def interest_expense(self):
        for val in USGAAP_INTERESTEXPENSE:
            if val in self.data:
                return self.data[val]
        return "--"

    def net_income(self):
        for val in USGAAP_NETINCOME:
            if val in self.data:
                return self.data[val]
        return "--"

    def operating_cf(self):
        for val in USGAAP_OPCASHFLOW:
            if val in self.data:
                return self.data[val]
        return "--"

    def excess_cash(self):
        return (
            self.normalize(self.operating_cf())
            - self.normalize(self.capex())
            - self.normalize(self.dividend())
            - self.normalize(self.interest_expense())
        )

    def capex(self):
        for val in USGAAP_CAPEX:
            if val in self.data:
                return self.data[val]
        return "--"

    def dividend(self):
        for val in USGAAP_DIVIDEND:
            if val in self.data:
                return self.data[val]
        return "--"
