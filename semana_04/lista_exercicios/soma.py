def main():

    numero = int(input("Digite um número inteiro: "))
    novo_numero = numero
    soma = 0

    if (novo_numero % 10 == 0):
        novo_numero = novo_numero // 10

    while novo_numero / 10 != 0:
        soma = soma + (novo_numero % 10)
        novo_numero = novo_numero // 10

    print(soma)


main()