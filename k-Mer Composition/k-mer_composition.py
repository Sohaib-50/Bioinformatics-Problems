def main():
    K = 4
    dna_string = get_data('rosalind_kmer.txt')
    kmers = get_lexicographically_sorted_kmers(['A', 'C', 'G', 'T'], K)
    kmer_composition = get_kmer_composition(dna_string, kmers) 

    write_solution_to_file('output.txt', kmer_composition)



def get_lexicographically_sorted_kmers(alphabet, k):
    '''Returns a list of all possible strings of length k using the letters in alphabet, sorted lexicographically'''
    ans = []

    def form_possible_strings(str_sofar):
        '''Recursively form all possible strings of length k starting with str_sofar'''

        # base case
        if len(str_sofar) == k:
            ans.append(str_sofar)
            return

        # recurse on all possible letters
        for j in range(len(alphabet)):
            form_possible_strings(str_sofar + alphabet[j])

    # form all possible strings starting with each letter in alphabet
    for i in range(len(alphabet)):
        form_possible_strings(alphabet[i])

    return ans


def count_substring_occurances(string, substring):
    '''returns number of times substring occurs in string'''
    count = 0
    l = len(substring)

    for i in range(len(string) - l + 1):
        if string[i : i + l] == substring:
            count += 1
    
    return count
    # '''returns number of times substring occurs in string using sliding window approach'''
    # count = 0
    # starting_positions =    []
    # start = 0
    # substring_index = 0

    # for end in range(len(string)):

    #     # slide open window
    #     if string[end] == substring[substring_index]:
    #         substring_index += 1
    #     else:
    #         substring_index = 0
    #         start = end  # slide close window

    #     # if window is opened to size of substring, it means substring is found
    #     if end - start + 1 == len(substring):
    #         count += 1
    #         starting_positions.append(start)
    #         start += 1
    #         substring_index -= 1  # because now window needs to become length substring - 1

    # return count, starting_positions


def get_kmer_composition(dna_string, k_mers):
    '''Returns a list of the number of times each k-mer appears in dna_string'''
    kmer_composition = []

    for k_mer in k_mers:
        # kmer_composition.append((count_substring_occurances(dna_string, k_mer)[0], count_substring_occurances(dna_string, k_mer)[1]))
        kmer_composition.append(count_substring_occurances(dna_string, k_mer))

    return kmer_composition


def get_data(file_name):
    with open(file_name, 'r') as f:
        f.readline()  # skip first line (fasta information)
        dna_string = ""
        for line in f:
            line = line.strip()
            dna_string += line
    return dna_string


def write_solution_to_file(file_name, kmer_composition):
    with open(file_name, 'w') as f:
        for count in kmer_composition:
            f.write(str(count) + " ")


if __name__ == '__main__':
    main()
