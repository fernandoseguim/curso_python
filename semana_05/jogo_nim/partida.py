from semana_05.jogo_nim.escolhe_jogada import usuario_escolhe_jogada, computador_escolhe_jogada


def partida():

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    winner = ""
    players = ["pc", "you"]
    next_player = "you"

    if (m + 1) % n == 0:
        print("\nVoce começa!")
        shot = usuario_escolhe_jogada(n,m)

        next_player = players[0]

    else:
        print("\nComputador começa!")
        shot = computador_escolhe_jogada(n,m)

    n = n - shot
    while n > 0 and winner == "":
        if next_player == players[1]:
            shot = usuario_escolhe_jogada(n, m)
            next_player = players[0]

            if n == shot:
                winner = players[1]
        else:
            shot = computador_escolhe_jogada(n, m)
            next_player = players[1]
            if n == shot:
                winner = players[0]
        n = n - shot

    if winner == players[0]:
        print("\nFim do jogo! O computador ganhou!")
    else:
        print("\nFim do jogo! Você ganhou!")
    
    return winner