def main():

    numero = int(input("Digite um número para ser decomposto em fatores: "))

    fator = 2
    multiplicidade = 0

    while (numero > 1):
        while (numero % fator == 0):
            multiplicidade = multiplicidade + 1
            numero = numero / fator

        if multiplicidade > 0:
            print("Fator %d, multiplicidade %d" % (fator, multiplicidade))
        fator = fator + 1
        multiplicidade = 0


main()