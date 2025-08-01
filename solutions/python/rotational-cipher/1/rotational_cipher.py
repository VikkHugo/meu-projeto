def rotate(text, key):
    texto_codificado = ''
    letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
    letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for letra in text:
        if letra in letras_minusculas:
            posicao = letras_minusculas.index(letra)
            nova_posicao = (posicao + key) % 26
            texto_codificado = texto_codificado + letras_minusculas[nova_posicao]
        elif letra in letras_maiusculas:
            posicao = letras_maiusculas.index(letra)
            nova_posicao = (posicao + key) % 26
            texto_codificado = texto_codificado + letras_maiusculas[nova_posicao]
        else:
            texto_codificado += letra
            
    return texto_codificado