def main():
    
    # get dataset from file (two fasta dna strings)
    dna0, dna1 = get_fasta_strings('rosalind_subo.txt')  

    # find the inexact repeat r in the two dna strings
    repeat = find_repeat(dna0, dna1)

    # count the number of times r appears in each dna string (with max 3 changes/indels)
    count_0 = count_repeat(dna0, repeat, 3)
    count_1 = count_repeat(dna1, repeat, 3)

    # show the results
    print(count_0, count_1)


def get_fasta_strings(file_name):
    '''reads all fasta dna sequences from a file and returns a list of them'''
    dna_list = []
    with open(file_name, 'r') as f:
        for line in f:
            if line[0] == '>':  # if line is start of a new dna string
                dna_list.append('')  # start a new dna string
            else:  # line is part of a dna string
                dna_list[-1] += line.strip()  # add line to the last dna string
    return dna_list


def substring_exists(s, sub):
    '''returns True if sub is a substring of s, False otherwise'''
    i = 0  # current index of s
    j = 0  # current index of sub
    
    while (i < len(s)) and (j < len(sub)):
        if s[i] == sub[j]:  # if current characters match
            j += 1  # move to next index of sub
        else:  # if current characters don't match
            j = 0  # reset j to 0 (start checking from beginning of sub)
        
        i += 1  # move to next index of s
    
    # if exited while loop due to j == len(sub), then sub is a substring of s because we reached the end of sub
    # otherwise, sub is not a substring of s
    if j == len(sub):
        return True
    else:
        return False


def find_repeat(dna0, dna1):
    '''returns the repeated string that occurs in both dna strings (of length 32-40)'''
    for i in range(32, 41):  # valid lengths of repeat
        for j in range(len(dna0) - i + 1):  # check all substrings of length i
            r = dna0[j : j + i]  # get a substring from dna0 (current index to current index + i)
            if substring_exists(dna1, r):  # if r is a substring of dna1
                return r  # return current substring
            

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
    
    # for every substring of length len(repeat) in dna
    for i in range((len(dna) - len(repeat) + 1)):
        current_substring = dna[ i : i + len(repeat)]  # slice dna from current index to current index + len(repeat) to get a substring of length len(repeat)
        
        if hamming_distance(current_substring, repeat) <= tolerance:  # if current substring of length len(repeat) has hamming distance <= tolerance
            count += 1
    return count


# driver code
if __name__ == '__main__':
    main()
