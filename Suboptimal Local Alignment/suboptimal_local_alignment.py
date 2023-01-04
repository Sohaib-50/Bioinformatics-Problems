def main():
    # get dataset from file
    data = get_fasta_strings('rosalind_subo.txt')
    dna0, dna1 = data[0], data[1]


    # find the inexact repeat r of 32-40 bp in the two dna strings that appears with slight modifications (each repeat differ by ≤3 changes/indels).
    repeat = find_repeat(dna0, dna1)

    # count the number of times r appears in each dna string with max 3 changes/indels
    count_0 = count_repeat(dna0, repeat, 3)
    count_1 = count_repeat(dna1, repeat, 3)

    # show the results
    print(count_0, count_1)


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


def find_repeat(dna0, dna1):
    '''finds the inexact repeat r of 32-40 bp in the two dna strings that appears with slight modifications (each repeat differ by ≤3 changes/indels).'''
    for i in range(32, 41):  # lengths of repeat
        for j in range(len(dna0) - i + 1):  # check all substrings of length i
            r = dna0[j : j + i]  # get the substring
            if r in dna1:  # if substring occurs in dna1
                return r


def hamming_distance(s1, s2):
    '''returns the hamming distance between two strings'''
    dist = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            dist += 1
    return dist + abs(len(s1) - len(s2))  # adding difference in length becaause extra characters are considered to be mismatches


def count_repeat(dna, repeat, tolerance=3):
    '''returns the number of times repeat appears in dna with max tolerance amount of changes/indels'''
    count = 0
    for i in range(len(dna) - len(repeat) + 1):
        if hamming_distance(dna[ i : i + len(repeat)], repeat) <= tolerance:  # if current substring of length len(repeat) has hamming distance <= tolerance
            count += 1
    return count


if __name__ == '__main__':
    main()
