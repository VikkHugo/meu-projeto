def is_valid(isbn):
    # Remove hífens e converte para maiúsculas (para tratar 'x' no final)
    clean_isbn = isbn.replace('-', '').upper()
    
    # Verifica se tem exatamente 10 caracteres
    if len(clean_isbn) != 10:
        return False
    
    total = 0
    for i in range(10):
        char = clean_isbn[i]
        # Verifica o último caractere (pode ser 'X')
        if i == 9 and char == 'X':
            value = 10
        elif not char.isdigit():
            return False
        else:
            value = int(char)
        
        # Calcula a soma ponderada
        total += value * (10 - i)
    
    # Verifica se é divisível por 11
    return total % 11 == 0