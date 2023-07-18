import requests
import os
from bs4 import BeautifulSoup
from edgar.parser import xbrlParser
from edgar.parser import getYYFromYYMMDD

BASE_URL = "https://www.sec.gov"


def fetchFiling(url):
    headers = {"User-Agent": "StockViewer Service stockviewer@unknown.com"}
    page = requests.get(
        url,
        headers=headers,
    )
    return page.content


def fetchDocuments(urls):
    docs = dict()
    for yy, url in urls.items():
        doc = fetchFiling(url)
        docs[yy] = doc
    return docs


def fetch10KURLs(ticker, years=None):
    search_url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type=10-K&dateb=&owner=exclude&count=10"
    ten_ks = fetchFiling(search_url.format(ticker))
    soup = BeautifulSoup(ten_ks, "lxml")
    table_tag = soup.find("table", class_="tableFile2", summary="Results")
    rows = table_tag.find_all("tr")
    ret = dict()
    for row in rows:
        cells = row.find_all("td")
        if len(cells) > 3 and cells[0].text == "10-K":
            yy = getYYFromYYMMDD(cells[3].text)
            if years == None or yy in years:
                ret[yy] = cells[1].a["href"]
    return ret


def getXBRLURL(doc):
    soup = BeautifulSoup(doc, "lxml")
    table_tag = soup.find("table", class_="tableFile", summary="Data Files")
    rows = table_tag.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        if len(cells) > 3:
            if (
                "INS" in cells[1].text
                or "INSTANCE" in cells[1].text
                or "INS" in cells[3].text
            ):
                return BASE_URL + cells[2].a["href"]


def fetchFiles(ticker):
    directory = "../data/"
    company = ticker + "/"
    xbrlFiles = os.listdir("../data/" + company)
    parsers = dict()
    for file in xbrlFiles:
        f = open(directory + company + file, "r+")
        xbrl_str = f.read()
        parser = xbrlParser(xbrl_str)
        parsers[parser.filingDate] = parser
    return parsers


def fetch(ticker, years=None):
    urls = fetch10KURLs(ticker, years)
    print(urls)
    xbrl_urls = dict()
    for yy, url in urls.items():
        tenk_doc = fetchFiling(BASE_URL + url)
        xurl = getXBRLURL(tenk_doc)
        xbrl_urls[yy] = xurl
    docs = fetchDocuments(xbrl_urls)
    return docs
