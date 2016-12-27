def main():

    n = int(input("Digite um número: "))
    lista_numeros = []

    while n > 0:
        lista_numeros.append(n)
        n = int(input("Digite um número: "))

    for i in range(1,len(lista_numeros)+1):
        print(lista_numeros[i*(-1)])


main()