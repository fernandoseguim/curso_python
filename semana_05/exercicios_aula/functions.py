import math

def fatorial(numero):

    f = 1;

    if numero < 0:
        return -1

    while numero > 0:
        f = f * numero
        numero = numero - 1

    return f

def pascal(n, k):

    p = fatorial(n) / (fatorial(k)*fatorial(n-k))

    return p

def delta(a, b, c):
    delta = b * b - (4 * a * c)
    return delta

def raizes(delta, b, a):
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    return x1, x2