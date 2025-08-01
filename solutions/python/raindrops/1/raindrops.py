def convert(number):
    som = ''
    if (number % 3 == 0):
        som = som + 'Pling'
    if (number % 5 == 0):
        som = som + 'Plang'
    if (number % 7 == 0):
        som = som + 'Plong'
    if (som == ''):
        som = str(number)
    return som
   
