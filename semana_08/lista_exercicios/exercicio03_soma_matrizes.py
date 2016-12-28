def soma_matrizes(matriz1, matriz2):

    if len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0]):
        matriz_soma = []

        for i in range(len(matriz1)):
            linha_soma = []
            for j in range(len(matriz1[i])):
                linha_soma.append(matriz1[i][j] + matriz2[i][j])
            matriz_soma.append(linha_soma)

        return matriz_soma
    else:
        return False
