def maior_elemento(lista):

    maior_elemento = lista[0]

    for i in lista:
        if i > maior_elemento:
            maior_elemento = i

    return maior_elemento