def main():
    a = int(input("Informe o valor de a: "))
    b = int(input("Informe o valor de b: "))
    c = int(input("Informe o valor de c: "))

    if ((a <= b) and (b <= c)):
        print ("crescente")
    else:
        print("não está em ordem crescente")

main()