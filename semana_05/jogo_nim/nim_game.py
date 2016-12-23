def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    winner = ""
    players = ["pc", "you"]
    next_player = "you"

    if n % (m + 1) == 0:
        print("\nVoce começa!")
        shot = usuario_escolhe_jogada(n, m)

        next_player = players[0]

    else:
        print("\nComputador começa!")
        shot = computador_escolhe_jogada(n, m)

    n = n - shot
    if  next_player == players[1] and n <= 0:
        winner = players[0]
    elif next_player == players[0] and n <= 0:
        winner = players[1]
    else:
        while n > 0 and winner == "":
            if next_player == players[1]:
                shot = usuario_escolhe_jogada(n, m)
                next_player = players[0]

                if n <= shot:
                    winner = players[1]
            else:
                shot = computador_escolhe_jogada(n, m)
                next_player = players[1]
                if n <= shot:
                    winner = players[0]
            n = n - shot

    if winner == players[0]:
        print("\nFim do jogo! O computador ganhou!")
    else:
        print("\nFim do jogo! Você ganhou!")

    return winner

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
    is_valid = True

    while shot < m and is_valid:
        if ((n - shot) % (m + 1)) == 0:
            is_valid = False
        else:
            shot = shot + 1

    print("\nO computador tirou %d peça." % (shot))

    return shot

def campeonato():

    you = 0
    pc = 0

    for i in range(1,4):
        print("**** Rodada %d ****" % (i))

        if partida() == "pc":
            pc = pc + 1
        else:
            you = you + 1


    print("** ** Final do campeonato! ** **")
    print("\nPlacar: Você %d X %d Computador" % (you, pc))

def main():

    opcao = int(input("Bem - vindo ao jogo do NIM! Escolha:\n\n"
                      "1 - para jogar uma partida isolada\n"
                      "2 - para jogar um campeonato "))

    if opcao == 1:
        print("\nVoce escolheu uma partida!!")
        partida()
    elif opcao == 2:
        print("\nVoce escolheu um campeonato!!")
        campeonato()
    else:
        print("\nOpção inválida!")

main()