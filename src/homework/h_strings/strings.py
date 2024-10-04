def get_hamming_distance(dna1, dna2):
    
    ham = 0
    num = 0
    for i in dna1:
        if dna1[num] != dna2[num]:
            ham += 1
        num += 1

    return(ham)



def get_dna_complement(dna):
    
    reverse = ''
    for i in dna:
        if i == 'A':
            reverse += 'T'
        elif i == 'T':
            reverse += 'A'
        elif i == 'C':
            reverse += 'G'
        elif i == 'G':
            reverse += 'C'

    count = -1
    for ch in reverse:
        count += 1

    final = ''
    while count > 0:
        for ch in reverse:
            final += reverse[count]
            count = count - 1 
    return final

