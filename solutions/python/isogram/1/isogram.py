def is_isogram(string):
    minuscula = string.lower()
    aparicoes = []
    
    for letra in minuscula:
        if letra in ['-', ' ']:
            continue
        if letra in aparicoes:
            return False
        aparicoes.append(letra)
    
    return True