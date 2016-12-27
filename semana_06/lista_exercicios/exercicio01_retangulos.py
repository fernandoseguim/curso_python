def retangulo(l,a):

    i = j = 0
    while i < a:
        while j < l:
            print("#", end="")
            j = j + 1
        print(end="\n")
        i = i + 1
        j = 0

def main():

    l = int(input("Digite a largura: "))
    a = int(input("Digite a altura: "))

    retangulo(l, a)

main()