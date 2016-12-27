from semana_07.lista_exercicios.exercicio03_maior_elemento import maior_elemento


def test_maior_elemento_positivo():
    lista = [10,51,6,7,2]
    assert maior_elemento(lista) == 51

def test_maior_elemento_negativo():
    lista = [-10, -51, -6, -7, -2]
    assert maior_elemento(lista) == -2