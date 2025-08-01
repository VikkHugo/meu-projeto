def translate(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = text.split()
    result = []

    for word in words:
        # Caso 1: Vogais, "yt", "xr" → add "ay"
        if (word[0] in vowels) or (word[:2] in {'yt', 'xr'}):
            translated = word + "ay"

        # Caso 2: "qu" ou consoante + "qu" → move "qu" para o final + "ay"
        elif 'qu' in word[:2] or (word[0] not in vowels and 'qu' in word[1:3]):
            qu_index = word.find('qu') + 2
            translated = word[qu_index:] + word[:qu_index] + "ay"

        # Caso 3: "y" como consoante no início (ex: "yellow")
        elif word[0] == 'y':
            translated = word[1:] + word[0] + "ay"

        # Caso 4: "y" como vogal (segunda letra, ex: "my")
        elif len(word) > 1 and word[1] == 'y':
            translated = word[1:] + word[0] + "ay"

        # Caso 5: Consoantes normais
        else:
            consonant_cluster = ''
            i = 0
            while i < len(word) and (word[i] not in vowels and word[i] != 'y'):
                consonant_cluster += word[i]
                i += 1
            translated = word[i:] + consonant_cluster + "ay"

        result.append(translated)

    return ' '.join(result)