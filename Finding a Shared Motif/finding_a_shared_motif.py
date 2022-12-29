def find_shared_motif(sequences):
    '''returns the longest shared motif in the given sequences'''

    def get_all_substrings(s):
        '''returns all substrings of s'''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                yield s[i:j]

    def is_substring_in_all(s, sequences):
        '''returns True if s is a substring of all sequences'''
        for seq in sequences:
            if s not in seq:
                return False
        return True
    
    # get all substrings of the first sequence
    substrings = get_all_substrings(sequences[0])

    # sort substrings by length
    substrings = sorted(substrings, key=len, reverse=True)

    # find the longest substring that is a substring of all sequences
    for s in substrings:
        if is_substring_in_all(s, sequences):
            return s
    

def get_sequences(file_name):
    with open(file_name, 'r') as f:
        current_seq = ''
        sequences = []
        for line in f:
            if line[0] == '>':
                if current_seq != '':
                    sequences.append(current_seq)
                    current_seq = ''
            else:
                current_seq += line.strip()
        sequences.append(current_seq)
    return sequences


sequences = get_sequences('rosalind_lcsm.txt')
ans = find_shared_motif(sequences)
print(ans)