def fatorial(numero):

    f = 1;

    if numero < 0:
        return -1

    while numero > 0:
        f = f * numero
        numero = numero - 1

    return f

def test_fatorial_negativo():
    assert fatorial(-10) == -1

def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorial1():
    assert fatorial(1) == 1

def test_fatorial2():
    assert fatorial(2) == 2

def test_fatorial3():
    assert fatorial(3) == 6

def test_fatorial4():
    assert fatorial(4) == 24

def test_fatorial5():
    assert fatorial(5) == 120

