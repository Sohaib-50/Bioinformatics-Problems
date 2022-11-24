def transcribe_DNA_to_RNA(DNA):
    RNA = []
    for i, nucleotide in enumerate(DNA):
        if nucleotide == 'T':
            RNA.append('U')
        else:
            RNA.append(nucleotide)

    return "".join(RNA)


        
with open('rosalind_rna.txt', 'r') as DNA_file:
    DNA_string = DNA_file.read().strip()

RNA_string = transcribe_DNA_to_RNA(DNA_string)
print(RNA_string)
