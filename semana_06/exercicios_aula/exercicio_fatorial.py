def fatorial(numero):

    fatorial = 1

    while numero > 1:
        fatorial = fatorial * numero
        numero = numero - 1

    return fatorial

def main():

    continua = True

    while continua:
        numero = int(input("Diegite um numero: "))

        if numero < 0:
            continua = False
            print("*** Programa interrompido ***")
        else:
            print(fatorial(numero))

main()
