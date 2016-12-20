def main():

    x = int(input("Informe um numero inteiro: "))

    if ((x%3 == 0) and (x%5 == 0)):
        print("FizzBuzz")
    else:
        print("%d" %(x))

main()
