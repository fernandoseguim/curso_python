def main():
    
    n = int(input("Digite um valor: "))
    result = 0
	
    while n != 0:
        result = result + n
        n = int(input("Digite um valor: "))
		
    print(result)

main()