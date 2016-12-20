def main():

    numero = int(input("Insira um numero: "))
    novo_numero = numero
    soma = 0

    if (novo_numero % 10 == 0):
        novo_numero = novo_numero // 10

    while novo_numero / 10 != 0:
        soma = soma + (novo_numero % 10)
        novo_numero = novo_numero // 10

    print("A soma dos algarismos que compõem o número %d é %d" % (numero,soma))



main()
