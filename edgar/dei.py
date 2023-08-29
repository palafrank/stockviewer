from edgar.tags import *
import numpy


class deiDB:
    def __init__(self, data):
        self.data = dict([])
        for key, val in data.items():
            self.data[key] = val

    def shares(self):
        if DEI_STOCKCOUNT in self.data:
            return numpy.int64(self.data[DEI_STOCKCOUNT])
        else:
            return "--"
