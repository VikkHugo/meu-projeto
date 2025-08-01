def value(colors):
    cores = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    color_one = colors[0]
    color_two = colors[1]
    for cor in cores: 
        if cor == color_one:
            primeiro_valor = cores.index(cor)
        if cor == color_two:
            segundo_valor = cores.index(cor)
    return primeiro_valor*10 + segundo_valor
