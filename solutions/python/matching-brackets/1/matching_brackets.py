def is_paired(input_string):
    pilha = []
    for elemento in input_string:
        if elemento == '(' or elemento == '[' or elemento == '{':  # Se for abertura
            pilha.append(elemento)
        elif elemento == ')':  # Se for fechamento ')'
            if not pilha or pilha[-1] != '(':  # Verifica se o topo é '('
                return False
            pilha.pop()
        elif elemento == ']':  # Se for fechamento ']'
            if not pilha or pilha[-1] != '[':  # Verifica se o topo é '['
                return False
            pilha.pop()
        elif elemento == '}':  # Se for fechamento '}'
            if not pilha or pilha[-1] != '{':  # Verifica se o topo é '{'
                return False
            pilha.pop()
    
    return len(pilha) == 0  # Pilha vazia = balanceado