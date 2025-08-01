def encode(plain_text):
    letras_minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    texto_codificado = ''
    contador = 0
    for letra in plain_text.lower().replace(' ',''):
        if letra in letras_minusculas:
            posicao = letras_minusculas.index(letra)
            nova_posicao = 25 - posicao
            letra_invertida = letras_minusculas[nova_posicao]
            texto_codificado = texto_codificado + letra_invertida
        else:
            if letra in numeros:
                texto_codificado = texto_codificado + letra
            else:
                continue
        if len(texto_codificado.replace(' ','')) % 5 == 0: 
            texto_codificado = texto_codificado + ' '
    return texto_codificado.strip()


def decode(ciphered_text):
    letras_minusculas =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    texto_decodificado = ''
    for letra in ciphered_text.lower().replace(' ',''):
        if letra in letras_minusculas:
            posicao_invertida = letras_minusculas.index(letra)
            posicao_correta = 25 - posicao_invertida
            texto_decodificado = texto_decodificado + letras_minusculas[posicao_correta]
        else:
            texto_decodificado = texto_decodificado + letra
    return texto_decodificado