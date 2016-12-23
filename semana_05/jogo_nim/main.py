from semana_05.jogo_nim.campeonato import campeonato
from semana_05.jogo_nim.partida import partida

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