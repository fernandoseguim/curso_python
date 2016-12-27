from semana_07.lista_exercicios.exercicio04_remove_repetidos import remove_repetidos


def test_remove_repetidos_1():
    lista = [7,3,33,12,3,3,3,7,12,100]
    lista2 = [1,2,4,5,51,100]
    assert remove_repetidos(lista) == lista2

