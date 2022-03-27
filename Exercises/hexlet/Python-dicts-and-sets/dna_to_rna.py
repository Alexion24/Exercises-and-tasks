def to_rna(dna):
    rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    result = ''
    for c in dna:
        result += rna[c]
    return result


print(to_rna('ACGTGGTCTTAA'))