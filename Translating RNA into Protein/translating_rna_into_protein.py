def RNA_to_protein(RNA):
    codon_table = {}
    with open('codon_table.txt', 'r') as f:
        for line in f:
            line = line.strip().split()
            for i in range(0, len(line), 2):
                codon_table[line[i]] = line[i + 1]

    protein = []
    for i in range(0, len(RNA), 3):
        codon = RNA[i : i + 3]  # pick 3 residues
        amino_acid = codon_table[codon]
        if amino_acid == "Stop":
            break
        protein.append(amino_acid)
    
    return "".join(protein)


with open('rosalind_prot.txt', 'r') as f:
    RNA = f.read().strip()


ans = RNA_to_protein(RNA)   
print(f"{ans}")