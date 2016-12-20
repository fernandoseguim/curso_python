def main():

    teste = False

    numero = int(input("Digite um número: "))
    num_aux = numero

    while num_aux // 10 != 0:

        aux = num_aux % 10
        num_aux = num_aux // 10

        if aux == num_aux % 10:
            teste = True

    if teste:
        print("O número %d contém algarismos adjacentes iguais!" % (numero))
    else:
        print("O número %d não contém algarismos adjacentes iguais!" % (numero))
main()