def cria_matriz(linhas, colunas, valor_inicial):

    '''(int, int, valor) -> matriz(lista de listas)
    Cria e retorna uma matriz com n linhas e n colunas em que cada elemento é igual ao valor inicial'''

    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(valor_inicial)
        matriz.append(linha)

    return matriz

def altera_valor_matriz(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input("Digite o novo valor para [%d][%d]: " %(i,j)))

    return matriz


def le_matriz():

    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))

    return cria_matriz(linhas, colunas, 0)

def imprime_matriz(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="")
        print()

def main():

    matriz = le_matriz()
    imprime_matriz(matriz)
    altera_valor_matriz(matriz)
    imprime_matriz(matriz)

main()