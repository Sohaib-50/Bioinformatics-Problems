def count_transitions_transversions(dna0, dna1):
    count_transitions = count_transversions = 0
    for i in range(len(dna0)):
        current_nucleotides = {dna0[i], dna1[i]}

        # if both nucleotides are different
        if len(current_nucleotides) != 1:  
            
            # if they are a transition pair
            if current_nucleotides in [{"A", "G"}, {"C", "T"}]:  
                count_transitions += 1

            # if they are a transversion pair
            else:  
                count_transversions += 1

    return count_transitions, count_transversions


def get_fasta_strings(file_name):
    '''reads all fasta dna sequences from a file and returns a list of them'''
    dna_list = []
    with open(file_name, 'r') as f:
        for line in f:
            if line[0] == '>':
                dna_list.append('')
            else:
                dna_list[-1] += line.strip()
    return dna_list
        
        
dna_list = get_fasta_strings('rosalind_tran.txt')
transitions, transversions = count_transitions_transversions(dna_list[0], dna_list[1])
print(transitions/transversions)