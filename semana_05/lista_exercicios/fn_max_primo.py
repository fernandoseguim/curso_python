def maior_primo(x):

    p_list = list_primos(x)

    maior = 0

    for i in p_list:
        maior = i
        if i > maior:
            maior = i

    return maior

def list_primos(x):

    primos = []

    i = 2

    while i <= x:

        if eh_primo(i):
            primos.append(i)
        i = i + 1

    return primos

def eh_primo(x):

    primo = True
    i = 2
    while i <= x:
        quociente = x / i
        resto = x % i

        if (resto == 0 and quociente >= i):
            primo = False
        i = i + 1

    return primo

