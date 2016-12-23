from semana_05.lista_exercicios.fn_maximo import maximo, maximo3


def test_maximo_x():
    assert maximo(4,3) == 4

def test_maximo_y():
    assert maximo(2, 3) == 3


def test_maximo3_x():
    assert maximo3(4,3,1) == 4

def test_maximo3_y():
    assert maximo3(2, 3, 1) == 3

def test_maximo3_z():
    assert maximo3(1,2,5) == 5