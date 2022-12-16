def get_protein_to_codon_counts():
    protein_to_codon_counts = {}
    with open('codon_table.txt', 'r') as f:
        for line in f:
            line = line.strip().split()
            for i in range(1, len(line), 2):
                protein_to_codon_counts[line[i]] = protein_to_codon_counts.get(line[i], 0) + 1
                
    return protein_to_codon_counts


def count_mrna_from_protein(protein):
    count = 1
    protein_to_codon_counts = get_protein_to_codon_counts()
    for amino_acid in protein:
        count = (count * protein_to_codon_counts[amino_acid]) % 1000000

    return count * protein_to_codon_counts["Stop"]


with open('rosalind_mrna.txt', 'r') as f:
    protein = f.read().strip()

ans = count_mrna_from_protein(protein)
print(ans)