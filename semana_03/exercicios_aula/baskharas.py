import math

def main():

    a = float(input("Informe o valor de ""a"": "))
    b = float(input("Informe o valor de ""b"": "))
    c = float(input("Informe o valor de ""c"": "))

    delta = b*b - (4 * a * c)

    if delta < 0:
        print("Esta equação não possui raízes reais!")

    elif delta == 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        print("Esta equação possui apenas a raíz %.2f" % (x1))

    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Esta equação possui as raízes %.2f e %.2f" % (x1,x2))

main()