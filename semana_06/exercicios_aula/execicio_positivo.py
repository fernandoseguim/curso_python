def main():

    continua = "S"

    while (str.upper(continua) == "S"):
        numero = float(input("Digite um numero: "))
        aux = int(numero)

        if (numero > 0 and aux == numero):
            print(True)

        else:
            print(False)

        continua = input("Deseja testar um outro número? (s ou n)")


main()