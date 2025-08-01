def rows(entrada):
    letras_maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letra =  entrada.upper()
    if letra in letras_maiusculas:
        indice = letras_maiusculas.index(letra)
        tamanho = 2*(indice + 1) - 1 
    else:
        return []
    diamante = []
    for i in range(tamanho):
        vetor_x = []
        for j in range(tamanho):
            vetor_x.append(' ')
        diamante.append(vetor_x)
    for letra in letras_maiusculas[:indice + 1]:
        if letra == 'A':
            diamante[0][indice] = 'A'
            diamante[tamanho - 1][indice] = 'A'
        elif letra == entrada.upper():
            diamante[indice][0] = letra
            diamante[indice][tamanho - 1] = letra
        else:
            posicao = letras_maiusculas.index(letra)
            linhas = [posicao,tamanho-1-posicao]
            colunas = [indice - posicao,indice+posicao]
            diamante[linhas[0]][colunas[0]] = letra
            diamante[linhas[0]][colunas[1]] = letra
            diamante[linhas[1]][colunas[0]] = letra
            diamante[linhas[1]][colunas[1]] = letra
    for i in range(tamanho):
        diamante[i] = ''.join(diamante[i])
    return diamante
