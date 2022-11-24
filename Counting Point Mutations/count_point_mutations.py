def count_point_mutations(DNA0, DNA1):
    hamming_distance = 0
    for i in range(len(DNA0)):
        if DNA0[i] != DNA1[i]:
            hamming_distance += 1
    return hamming_distance

        
with open('rosalind_hamm.txt', 'r') as DNA_file:
    DNA0 = DNA_file.readline().strip()
    DNA1 = DNA_file.readline().strip()
    
point_mutations = count_point_mutations(DNA0, DNA1)
print(point_mutations)
