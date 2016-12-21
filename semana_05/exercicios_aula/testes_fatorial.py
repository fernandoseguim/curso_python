from semana_05.exercicios_aula.functions import fatorial


def teste_fatorial():

    if fatorial(0) == 1:
        print("Função fatorial funcionou para 0")
    else:
        print("Função fatorial não funcionou para 0")

    if fatorial(1) == 1:
        print("Função fatorial funcionou para 1")
    else:
        print("Função fatorial não funcionou para 1")

    if fatorial(2) == 2:
        print("Função fatorial funcionou para 2")
    else:
        print("Função fatorial não funcionou para 2")

    if fatorial(3) == 6:
        print("Função fatorial funcionou para 3")
    else:
        print("Função fatorial não funcionou para 3")

    if fatorial(4) == 24:
        print("Função fatorial funcionou para 4")
    else:
        print("Função fatorial não funcionou para 4")

    if fatorial(5) == 120:
        print("Função fatorial funcionou para 5")
    else:
        print("Função fatorial não funcionou para 5")

    if fatorial(-1) == 120:
        print("Função fatorial funcionou para 5")
    else:
        print("Função fatorial não funcionou para 5")

    fatorial(-1)

teste_fatorial()