from calculator import add, sub, sqrt, multiply, power, divide, log

def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6


def test_sqrt():
    assert sqrt(4) == 2

    
def test_divide():
    assert divide(12, 4) == 3
    assert divide(20, 2) == 10


def test_power():
    assert power(2, 2) == 4
    assert power(2, 3) == 8


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0


def test_log():
    assert abs(log(100, 10) - 2.0) < 1e-9
    assert abs(log(8, 2) - 3.0) < 1e-9
    assert abs(log(1, 5) - 0.0) < 1e-9
    assert abs(log(0.5, 2) - (-1.0)) < 1e-9
    
