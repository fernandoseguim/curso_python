def main():

    numero = int(input("Digite um numero: "))

    soma_hipotenusas = 0

    for hipotenusa in range(1,numero+1):

        for cateto1 in range(1, hipotenusa):
            cateto2 = cateto1
            while(cateto1*cateto1 + cateto2*cateto2 < hipotenusa*hipotenusa):
                cateto2 = cateto2 + 1
            if (cateto1*cateto1 + cateto2*cateto2 == hipotenusa*hipotenusa):
                soma_hipotenusas = soma_hipotenusas + hipotenusa


    return soma_hipotenusas

main()