'''
def square(number):
    if (number <= 0 or number > 64):
        raise ValueError("O número de quadrados deve estar entre 1 e 64")
    return 2**(number-1)

def total():
    return (2**64) - 1
'''

def square(number):
    # Verifica se é um inteiro positivo entre 1 e 64
    if not isinstance(number, int) or number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

def total():
    return (2 ** 64) - 1  # Soma de todos os quadrados (1+2+4+...+2^63)