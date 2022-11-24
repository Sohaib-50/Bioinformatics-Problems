def count_DNA_nucleotides(DNA_string):
    nucleotide_counts = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
    }
    for nucleotide in DNA_string:
        nucleotide_counts[nucleotide] += 1

    return nucleotide_counts


with open('rosalind_dna.txt', 'r') as DNA_file:
    DNA_string = DNA_file.read().strip()

nucleotide_counts = count_DNA_nucleotides(DNA_string)
print(nucleotide_counts)
print(list(nucleotide_counts.values()))