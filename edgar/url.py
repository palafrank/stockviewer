def build10KListURL(ticker):
    searchURL = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type=10-K&dateb=&owner=exclude&count=10"
    print(searchURL.format(ticker))
