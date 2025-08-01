def is_armstrong_number(number):
    # Converte o número em string para contar dígitos e manipular cada um
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calcula a soma dos dígitos elevados ao número de dígitos
    sum_armstrong = sum(int(digit) ** num_digits for digit in num_str)
    
    # Verifica se a soma é igual ao número original
    return sum_armstrong == number
