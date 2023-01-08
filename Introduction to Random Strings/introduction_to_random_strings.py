from math import log10

def solution(data):
    dna_string, A = data
    B = []
    gc_count = dna_string.count('G') + dna_string.count('C')
    at_count = dna_string.count('A') + dna_string.count('T')

    for gc_content in A:
        B.append( (gc_count * log10(gc_content / 2)) + (at_count * log10((1 - gc_content) / 2)) )

    return B



def get_data(file_name):
    with open(file_name, 'r') as f:
        dna_string = f.readline().strip()
        A = f.readline().strip().split()
        A = [float(x) for x in A]
    return dna_string, A


data = get_data('rosalind_prob.txt')
ans = solution(data)
with open('output.txt', 'w') as f:
    f.write(" ".join([str(x) for x in ans]))