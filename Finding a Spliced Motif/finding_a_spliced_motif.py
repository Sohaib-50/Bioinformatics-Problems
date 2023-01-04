def get_subsequence_indices(s, t):
    '''returns any set indices of s where the character of s is same as t'''
    indices = []
    t_index = s_index = 0
    while (s_index < len(s)) and (t_index < len(t)):
        if s[s_index] == t[t_index]:
            indices.append(s_index + 1)
            t_index += 1
        
        s_index += 1

    return indices


def get_fasta_strings(file_name):
    '''reads all fasta dna sequences from a file and returns a list of them'''
    dna_list = []
    with open(file_name, 'r') as f:
        for line in f:
            if line[0] == '>':
                dna_list.append('')  # start a new dna string
            else:
                dna_list[-1] += line.strip()  # add to the last dna string
    return dna_list


s, t = get_fasta_strings('rosalind_sseq.txt')
indices = get_subsequence_indices(s, t)
print(" ".join([str(i) for i in indices]))