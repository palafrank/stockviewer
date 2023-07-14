import requests
import os
import sys
from bs4 import BeautifulSoup
from gaap import gaapDB
from report import fundamentals
from tags import *


def getYYFromYYMMDD(date_str):
    splits = date_str.split("-")
    return splits[0]


class xbrlParser:
    """Parser for XBRL document"""

    def getContextYear(self, tag):
        if tag.get(CONTEXT_REFERENCE1) != None:
            ctx = tag[CONTEXT_REFERENCE1]
        elif tag.get(CONTEXT_REFERENCE2) != None:
            ctx = tag[CONTEXT_REFERENCE2]
        else:
            return ""
        if ctx in self.contexts:
            return self.contexts[ctx]
        return ""

    def num_months(self, start_month, start_year, end_month, end_year):
        if start_year == end_year:
            return int(end_month) - int(start_month)
        else:
            years = int(end_year) - int(start_year)
            add_months = 12 * (int(years) - 1)
            a = 12 - int(start_month)
            extra_months = int(end_month) + a
            return extra_months + add_months

    def contextParser(self):
        self.contexts = dict()
        prefix = ""
        contexts = self.soup.find_all("xbrli:context")
        if len(contexts) > 0:
            prefix = "xbrli:"
        else:
            contexts = self.soup.find_all("context")
            if contexts == 0:
                sys.exit("failed to find filing context")
        for tag in contexts:
            if tag.find(prefix + "entity") != None:
                if tag.find(prefix + "segment") != None:
                    continue
            if tag.find(prefix + "period") != None:
                if tag.find(prefix + "endDate") != None:
                    end_splits = tag.find(prefix + "endDate").text.split("-")
                    start_splits = tag.find(prefix + "startDate").text.split("-")
                    if (
                        self.num_months(
                            start_splits[1],
                            start_splits[0],
                            end_splits[1],
                            end_splits[0],
                        )
                        >= 11
                    ):
                        self.contexts[tag["id"]] = end_splits[0]
                elif tag.find(prefix + "instant") != None:
                    splits = tag.find(prefix + "instant").text.split("-")
                    self.contexts[tag["id"]] = splits[0]
                else:
                    sys.exit(tag + " :no end-date/instant found while parsing context")
            else:
                sys.exit(tag + " :no period found while parsing context", tag.name)
        print("Selected contexts: ", self.contexts)

    def initParser(self):
        cells = self.soup.find_all(DEI_FILINGDATE)
        if len(cells) > 0:
            self.filingDate = getYYFromYYMMDD(cells[0].text)
        else:
            sys.exit("failed to find filing date")
        self.contextParser()

    def gaapTags(self):
        gaapData = dict([])
        soup = BeautifulSoup(self.doc, "lxml")
        tags = soup.find_all()
        for tag in tags:
            if "us-gaap" in tag.name:
                if self.getContextYear(tag) == self.filingDate:
                    gaapData[tag.name.lower()] = tag.text
        self.gaap = gaapDB(gaapData)

    def __init__(self, xbrlDoc):
        self.doc = xbrlDoc
        self.soup = BeautifulSoup(self.doc, "xml")
        self.initParser()
        print(self.filingDate)
        self.gaapTags()


"""
directory = "../data/"
company = "IBM/"
xbrlFiles = os.listdir("../data/" + company)
file_name = "2014.xml"

df = fundamentals()

f = open(directory + company + file_name, "r+")
xbrl_str = f.read()
parser = xbrlParser(xbrl_str)
df.insert(parser)
df.print()
"""
