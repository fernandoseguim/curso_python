def usuario_escolhe_jogada(n,m):

    shot = int(input("\nQuantas peças você vai tirar? "))
    is_valid = False

    while not is_valid:

        if shot <= m:
            is_valid = True
        else:
            print("\nOops! jogada inválida! Tente de novo.")
            shot = int(input("\nQuantas peças você vai tirar? "))


    print("\nVocê tirou %d peça." % (shot))

    return shot


def computador_escolhe_jogada(n,m):

    shot = 1

    if n == m:
        shot = m
    elif n < m:
        shot = n

    print("\nO computador tirou %d peça." % (shot))

    return shot

