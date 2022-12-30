import os

def get_coding_region(dna_string, introns):
    for intron in introns:
        dna_string = dna_string.replace(intron, '')
    return dna_string


def transcribe_DNA_to_RNA(dna_string):
    rna = []
    for i, nucleotide in enumerate(dna_string):
        if nucleotide == 'T':
            rna.append('U')
        else:
            rna.append(nucleotide)

    return "".join(rna)


def get_codon_table():
    codon_table = {}
    # open and read the codon table file from parent directory
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



def get_data(file_name):
    with open(file_name, 'r') as f:
        f.readline()
        dna_string = ""
        for line in f:
            if line[0] == '>':
                break
            dna_string += line.strip()

        introns = []
        current_intron = ""
        for line in f:
            if line[0] == '>':
                introns.append(current_intron)
                current_intron = ""
            else:
                current_intron += line.strip()
        introns.append(current_intron)
    
    return dna_string, introns


data = get_data('rosalind_splc.txt')
coding_region = get_coding_region(dna_string = data[0], introns = data[1])
final_rna =  transcribe_DNA_to_RNA(dna_string=coding_region)
protein_string = translate_RNA_to_protein(rna=final_rna)
print(protein_string)