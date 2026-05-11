def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def ln(x, terms=100):
    """Logaritme natural utilitzant la sèrie de Taylor de ln((1+t)/(1-t))."""
    if x <= 0:
        raise ValueError("L'argument ha de ser positiu")
    
    # Reducció: ln(x) = ln(m * 2^k) = ln(m) + k*ln(2)
    k = 0
    while x >= 2:
        x /= 2
        k += 1
    while x < 1:
        x *= 2
        k -= 1

    # Ara x ∈ [1, 2), utilitzem t = (x-1)/(x+1) i la sèrie ln(x) = 2*(t + t³/3 + t⁵/5 + ...)
    t = (x - 1) / (x + 1)
    t_sq = t * t
    term = t
    result = 0.0
    for n in range(terms):
        result += term / (2 * n + 1)
        term *= t_sq

    LN2 = 0.6931471805599453  # constant precalculada
    return 2 * result + k * LN2


def log(a, b):
    """Logaritme de 'a' en base 'b'."""
    if b <= 0 or b == 1:
        raise ValueError("La base ha de ser positiva i diferent d'1")
    if a <= 0:
        raise ValueError("L'argument ha de ser positiu")
    return ln(a) / ln(b)