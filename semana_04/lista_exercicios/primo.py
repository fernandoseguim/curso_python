def main():

    numero = int(input("Digite um número inteiro: "))
    primo = True

    i = 2
    while i <= numero and primo:
        quociente = numero / i
        resto = numero % i

        if (resto == 0 and quociente >= i):
            primo = False
        i = i + 1

    if primo and (numero != 1):
        print("primo")
    else:
        print("nao primo")

main()