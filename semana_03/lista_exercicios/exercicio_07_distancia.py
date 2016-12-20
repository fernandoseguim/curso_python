import math


def main():

    x1 = int(input("informe o valor de x1: "))
    y1 = int(input("informe o valor de y1: "))
    x2 = int(input("informe o valor de x2: "))
    y2 = int(input("informe o valor de y2: "))

    d2 = (x2 - x1)**2 + (y2 - y1)**2

    d = math.sqrt(d2)

    if d >= 10:
        print("longe")
    else:
        print("perto")

main()