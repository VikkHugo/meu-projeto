def label(colors):
    cores = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    color_one = colors[0]
    color_two = colors[1]
    color_three = colors[2]
    for cor in cores: 
        if cor == color_one:
            primeiro_valor = cores.index(cor)
        if cor == color_two:
            segundo_valor = cores.index(cor)
        if cor == color_three:
            terceiro_valor = cores.index(cor)
    resistencia = (primeiro_valor*10 + segundo_valor)*10**terceiro_valor
    if resistencia >= 1000000000:
        return str(int(resistencia/1000000000))+' '+'gigaohms'
    if resistencia >= 1000000:
        return str(int(resistencia/1000000))+' '+'megaohms'
    if resistencia >= 1000:
        return str(int(resistencia/1000))+' '+'kiloohms'
    if resistencia < 1000:
        return str(resistencia)+' '+'ohms'