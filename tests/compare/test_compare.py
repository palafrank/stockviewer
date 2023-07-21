import yahoofinance.compare as compare

def test_compare():
    data = compare.comparator(["AAPL", "MSFT", "META"]).info()
    assert data is not None
    assert len(data) == 3
    assert data.at[0, "symbol"] == "AAPL"
    assert data.at[1, "symbol"] == "MSFT"
    assert data.at[2, "symbol"] == "META"
    assert data.at[0, "marketCap"] > 0
    assert data.at[1, "marketCap"] > 0
    assert data.at[2, "marketCap"] > 0
    assert data.at[0, "totalRevenue"] > 0   
    assert data.at[1, "totalRevenue"] > 0
    assert data.at[2, "totalRevenue"] > 0
    assert data.at[0, "grossProfits"] > 0
    assert data.at[1, "grossProfits"] > 0
    assert data.at[2, "grossProfits"] > 0
    assert data.at[0, "ebitda"] > 0
    assert data.at[1, "ebitda"] > 0
    assert data.at[2, "ebitda"] > 0