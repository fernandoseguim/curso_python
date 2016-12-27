def primo(numero):
    primo = True
    i = 2

    if numero == 1:
        primo = False

    else:
        while i <= numero and primo:
            quociente = numero / i
            resto = numero % i

            if (resto == 0 and quociente >= i):
                primo = False
            i = i + 1

    return primo

def n_primos(numero):

    quantidade = 0

    if (numero > 0):
        while numero > 1:
            if primo(numero):
                quantidade = quantidade + 1
            numero = numero - 1

        return quantidade

    else:
        return -1

def main():

    n = int(input("Digite um numero inteiro e positivo maior que 2: "))

    print(n_primos(n))

main()