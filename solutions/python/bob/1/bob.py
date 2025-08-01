def response(hey_bob):
    # Remove espaços extras e verifica se está vazio (silêncio)
    stripped = hey_bob.strip()
    if not stripped:
        return "Fine. Be that way!"
    
    # Verifica se é um grito (tudo em maiúsculas e contém letras)
    is_shout = stripped.isupper() and any(c.isalpha() for c in stripped)
    # Verifica se é pergunta (termina com ?)
    is_question = stripped.endswith('?')
    
    if is_shout and is_question:
        return "Calm down, I know what I'm doing!"
    if is_shout:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever."