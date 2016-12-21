from semana_05.exercicios_aula.functions import delta, raizes


def main():

    a = float(input("Informe o valor de ""a"": "))
    b = float(input("Informe o valor de ""b"": "))
    c = float(input("Informe o valor de ""c"": "))

    d = delta(a,b,c)

    if d < 0:
        print("Esta equação não possui raízes reais!")

    elif d == 0:
        x1, x2 = raizes(d, a, b)
        print("Esta equação possui apenas a raíz %.2f" % (x1))

    else:
        x1, x2 = raizes(d, a, b)
        print("Esta equação possui as raízes %.2f e %.2f" % (x1, x2))

main()
