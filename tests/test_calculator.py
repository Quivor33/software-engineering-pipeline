from calculator import add, sub, multiply, log

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(10, 4) == 6
    
from calculator import add, sub, multiply

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0

def test_log():
    assert abs(log(100, 10) - 2.0) < 1e-9
    assert abs(log(8, 2)   - 3.0) < 1e-9
    assert abs(log(1, 5)   - 0.0) < 1e-9
    assert abs(log(0.5, 2) - (-1.0)) < 1e-9