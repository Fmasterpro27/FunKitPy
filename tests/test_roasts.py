from funkitpy import roast, get_roast

def test_roast():
    assert isinstance(roast(), str)

def test_get_roast():
    assert isinstance(get_roast(), str)
