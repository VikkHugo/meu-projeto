def to_rna(dna_strand):
    sequencia = ''
    molecula = ''
    if dna_strand == 'A':
        molecula = 'U'
    if dna_strand == 'C':
        molecula = 'G'
    if dna_strand == 'G':
        molecula = 'C'
    if dna_strand == 'T':
        molecula = 'A'
    if dna_strand == '':
        molecula = ''
    if len(dna_strand) > 1:
        for indice in dna_strand:
            molecula = ''
            if indice == 'A':
                molecula = 'U'
            if indice == 'C':
                molecula = 'G'
            if indice == 'G':
                molecula = 'C'
            if indice == 'T':
                molecula = 'A'
            sequencia = f'{sequencia}{molecula}'
        return sequencia
    else: 
        return molecula            
