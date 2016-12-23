from semana_05.jogo_nim.partida import partida


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

