def imprime_matriz(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == len(matriz[i])-1:
                print(matriz[i][j], end="")
            else:
                print(matriz[i][j], end=" ")
        print()




def main():

    matriz = []
    linha = [1,2,3]

    for i in range(len(linha)):
        matriz.append(linha)

    imprime_matriz(matriz)

main()