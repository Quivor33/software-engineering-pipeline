from calculator import add, sub, divide

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(10, 4) == 6

def test_divide():
    assert divide(12, 4) == 3
    assert divide(20, 2) == 10