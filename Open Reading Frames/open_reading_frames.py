import os.path

START_CODON = "AUG"
STOP_CODONS = {"UAA", "UAG", "UGA"}


def read_dna():
    with open('rosalind_orf.txt', 'r') as f:
        f.readline()  # skip first line
        dna = f.read().replace("\n", "").strip()  # read in the rest of the file
    return dna


def reverse_complement(dna):
    dna = dna[::-1]  # reverse the string
    dna = dna.replace("A", "t")
    dna = dna.replace("T", "a")
    dna = dna.replace("C", "g")
    dna = dna.replace("G", "c")
    dna = dna.upper()
    return dna


def transcribe_DNA_to_RNA(dna):
    RNA = []
    for i, nucleotide in enumerate(dna):
        if nucleotide == 'T':
            RNA.append('U')
        else:
            RNA.append(nucleotide)
    return "".join(RNA)


def get_ORFs(rna):
    orfs = []
    current_search_start = rna.find(START_CODON)
    i = current_search_start
    while (i < len(rna)) and (i != -1):

        # if a stop codon is reached, add it to list of ORFs
        if rna[i: i + 3] in STOP_CODONS:
            orfs.append(rna[current_search_start: i + 3])
            current_search_start = rna.find(START_CODON, current_search_start + 3)
            i = current_search_start

        else:
            i += 3  # move ahead length of a codon

    # if currently at a stop codon, add it to list of ORFs
    if rna[i: i + 3] in STOP_CODONS:
        orfs.append(rna[current_search_start: i + 3])

    return orfs


def get_codon_table():
    codon_table = {}
    # open the codon table file from parent directory
    with open(os.path.dirname(__file__) + '/../codon_table.txt', 'r') as f:
        for line in f:
            line = line.strip().split()
            for i in range(0, len(line), 2):
                codon_table[line[i]] = line[i + 1]
    return codon_table


def translate_RNA_to_protein(rna):
    codon_table = get_codon_table()
    protein = []
    for i in range(0, len(rna), 3):
        codon = rna[i: i + 3]  # pick 3 residues
        amino_acid = codon_table[codon]
        if amino_acid == "Stop":
            break
        protein.append(amino_acid)

    return "".join(protein)


def get_protein_from_ORFs(orfs):
    proteins = []
    for orf in orfs:
        proteins.append(translate_RNA_to_protein(orf))
    return proteins


def main():
    dna = read_dna()  # read in the DNA string from file
    dna_reverse_complement = reverse_complement(dna)

    # transcribe the DNA strings to RNA
    rna = transcribe_DNA_to_RNA(dna)
    rna_reverse_complement = transcribe_DNA_to_RNA(dna_reverse_complement)

    orfs = get_ORFs(rna) + get_ORFs(rna_reverse_complement)  # get ORFs for both DNA strands

    proteins = set(get_protein_from_ORFs(orfs))

    # write the proteins to file
    with open('output1.txt', 'w') as f:
        f.write("\n".join(proteins))



if __name__ == "__main__":
    main()
