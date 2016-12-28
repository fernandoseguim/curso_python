def sao_multiplicaveis(matriz1,matriz2):

    num_colunas_matriz1 = len(matriz1[0])
    num_linhas_matriz2 = len(matriz2)

    if num_colunas_matriz1 == num_linhas_matriz2:
        return True
    else:
        return False

