def main():

    teste = False

    numero = int(input("Digite um número inteiro: "))
    num_aux = numero

    while num_aux // 10 != 0:

        aux = num_aux % 10
        num_aux = num_aux // 10

        if aux == num_aux % 10:
            teste = True

    if teste:
        print("sim")
    else:
        print("nao")
main()