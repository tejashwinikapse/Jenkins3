from evenodd import evenandodd

def test_odd():
    assert evenandodd(2) == "Even"
    assert evenandodd(3) == "Odd"
def test_even():    
    assert evenodd(4) == "Odd"
    assert evenodd(5) == "Even"

