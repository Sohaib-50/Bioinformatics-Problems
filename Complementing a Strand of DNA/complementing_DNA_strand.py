def complement_DNA_strand(strand):
    complement = []
    nucleotide_complements = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    for i in range(len(strand) - 1, -1, -1):
        complement.append(nucleotide_complements[strand[i]])
    
    return "".join(complement)
        
with open('rosalind_revc.txt', 'r') as DNA_file:
    DNA_string = DNA_file.read().strip()

complement_strand = complement_DNA_strand(DNA_string)
print(complement_strand)
