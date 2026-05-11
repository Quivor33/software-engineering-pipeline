from calculator import add, sub

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(10, 4) == 6

def test_power():
    assert power(2, 2) == 4
    assert power(2, 3) == 8