def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No es pot dividir per 0"