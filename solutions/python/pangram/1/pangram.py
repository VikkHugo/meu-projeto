def is_pangram(sentence):
    contador = 0
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letra in letras: 
        if letra in sentence.lower():
            contador = contador + 1
    return  contador == len(letras)