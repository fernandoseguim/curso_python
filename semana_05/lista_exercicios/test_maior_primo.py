from semana_05.lista_exercicios.fn_max_primo import maior_primo


def test_maior_primo_test_1():
    assert maior_primo(100) == 97

def test_maior_primo_test_2():
    assert maior_primo(7) == 7