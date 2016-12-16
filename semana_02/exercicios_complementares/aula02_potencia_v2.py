def main():
    
    n = int(input("Digite o valor de n:"))
    p = int(input("Digite o valor de k:"))
    
    result = 1
    i = 1

    while i <= p:
        result = result * n
        i = i + 1

    print(result)
    
main()