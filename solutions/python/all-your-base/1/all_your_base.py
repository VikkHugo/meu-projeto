def rebase(input_base, digits, output_base):
    resultado = 0
    saida = []
    digito_invertido = digits.copy()
    digito_invertido.reverse()
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for indice in range(len(digito_invertido)):
        if digito_invertido[indice] < 0 or digito_invertido[indice] >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        resultado = resultado + (digito_invertido[indice]*(input_base**indice))
    while resultado >= output_base and resultado > 0:
        valor = int(resultado % output_base)
        resultado = int(resultado / output_base)
        saida.append(valor)
    saida.append(resultado)
    saida.reverse()
    return saida