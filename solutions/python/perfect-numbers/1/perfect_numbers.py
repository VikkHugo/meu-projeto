def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    divisores_do_alvo = []

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        for i in range(1, number + 1):
            if number % i == 0:
                divisores_do_alvo.append(i)
    if number > 0: 
        soma_dos_divisores = sum(divisores_do_alvo) - number 
        if soma_dos_divisores == number:
            return 'perfect'
        elif soma_dos_divisores > number:
            return 'abundant'
        else:
            return 'deficient'
