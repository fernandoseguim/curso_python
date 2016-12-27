def main():

    n = int(input("Digite um número: "))
    lista_numeros = []

    while n > 0:
        lista_numeros.append(n)
        n = int(input("Digite um número: "))

    i = len(lista_numeros) - 1
    while i >= 0:
        print(lista_numeros[i])
        i = i - 1

main()