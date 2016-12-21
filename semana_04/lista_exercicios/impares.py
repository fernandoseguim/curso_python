def main():

    numero = int(input("Digite o valor de n: "))

    i = 1

    while i < (numero * 2):
        if i % 2 != 0:
            print(i)
        i = i + 1

main()

