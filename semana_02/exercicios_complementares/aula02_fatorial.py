def main():
    
    n = int(input("Digite um numero para ser fatorado: "))
    result = 1

    while n > 0:
        result = result * n
        n = n - 1

    print(result)

main()