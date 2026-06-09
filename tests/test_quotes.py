def test_quotes():
    from funkitpy import quote

    assert isinstance(quote(), str)

def test_quote_data():
    from funkitpy import quote_data

    data = quote_data()

    assert isinstance(data, dict)
    assert "id" in data
    assert "quote" in data
    assert "author" in data