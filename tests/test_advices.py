def test_advice():
    from funkitpy import advice

    assert isinstance(advice(), str)