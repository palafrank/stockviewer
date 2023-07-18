import edgar.fetcher as fetcher

def test_fetchFiling():
    fetched = fetcher.fetch10KURLs("AAPL", ["2019", "2020"])
    assert fetched is not None
    assert len(fetched) == 2
    assert fetched["2019"] is not None
    assert fetched["2020"] is not None
    assert fetched["2020"] == "/Archives/edgar/data/320193/000032019320000096/0000320193-20-000096-index.htm"
    assert fetched["2019"] == "/Archives/edgar/data/320193/000032019319000119/0000320193-19-000119-index.htm"
    fetched = fetcher.fetch10KURLs("AAPL")
    assert fetched is not None
    assert len(fetched) == 10