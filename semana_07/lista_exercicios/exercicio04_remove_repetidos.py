def remove_repetidos(lista):

    lista = ordena(lista)

    for i in range(len(lista)-2):

        if lista[i] == lista[i + 1]:
            del lista[i]

    return lista

def ordena(lista):

    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if(lista[j] > lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

    return lista
