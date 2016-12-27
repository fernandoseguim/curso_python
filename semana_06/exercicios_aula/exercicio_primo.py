def positivo(numero):

    aux = int(numero)

    if (numero > 0 and aux == numero):
        return True
    else:
        return False

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

def main():

    numero = int(input("Digite um número inteiro e positivo: "))

    while positivo(numero):

        if primo(numero):
            print(numero, "é primo")
        else:
            print(numero, "não é primo")

        numero = int(input("Digite um número inteiro e positivo: "))

main()