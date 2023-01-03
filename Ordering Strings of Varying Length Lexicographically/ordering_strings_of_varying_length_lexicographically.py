def get_lexicographically_sorted_kmers(alphabet, k):
    ans = []

    def form_possible_strings(str_sofar):
        '''Recursively form all possible strings of length k starting with str_sofar'''
        ans.append(str_sofar)

        # base case
        if len(str_sofar) == k:
            return

        # recurse on all possible letters
        for j in range(len(alphabet)):
            form_possible_strings(str_sofar + alphabet[j])


    # form all possible strings starting with each letter in alphabet
    for i in range(len(alphabet)):
        form_possible_strings(alphabet[i])

    return ans


def get_data(file_name):
    with open(file_name, 'r') as f:
        alphabet = f.readline().strip().split()
        k = int(f.readline().strip())
    return alphabet, k


alphabet, k = get_data('rosalind_lexv.txt')  # get data from file
ans = get_lexicographically_sorted_kmers(alphabet, k)  # get lexicographically sorted kmers

# write output to file
with open('output.txt', 'w') as f:
    for i in range(len(ans)):
        f.write(ans[i] + '\n')