def main():

    # get dataset
    DATASET_FILE = "rosalind_lcsq.txt"
    data = get_fasta_strings(DATASET_FILE)
    dna_string0 = data[0]
    dna_string1 = data[1]

    # compute the dynamic programming matrix for longest common subsequence lengths
    lcs_lengths_dp_matrix = get_lcs_lengths_dp_matrix(dna_string0, dna_string1, display=False)

    # find out the longest common subsequence
    lcs = get_lcs(dna_string0, dna_string1, lcs_lengths_dp_matrix)

    print(f"The longest common subsequence / shared spliced motif is:")
    print(lcs)


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


def get_lcs_lengths_dp_matrix(string0, string1, display=False):
    '''
    returns a matrix of longest common subsequence lengths
    and prints the matrix if display is True
    '''
    rows = len(string0) + 1
    cols = len(string1) + 1
    matrix = [ [0 for i in range(cols)] for j in range(rows) ]  # initialize matrix with zeros

    # fill in the matrix
    for x in range(1, rows):
        for y in range(1, cols):
            
            # if current position in string0 and string1 are the same,
            # then the longest common subsequence length at this position is
            # the longest common subsequence length at the diagonal position behind + 1
            if string0[x - 1] == string1[y - 1]:
                matrix[x][y] = matrix[x - 1][y - 1] + 1
            
            # otherwise, the longest common subsequence length at this position is
            # the maximum of the longest common subsequence length at the position above and
            # the longest common subsequence length at the position to the left
            else:
                if matrix[x - 1][y] > matrix[x][y - 1]:
                    matrix[x][y] = matrix[x - 1][y]
                else:
                    matrix[x][y] = matrix[x][y - 1]
    
    # print out the matrix if display is True
    if display:
        print("Longest Common Subsequence Lengths Matrix:")

        # print row labels
        print("    ", end="")
        for i in range(len(string1)):
            print(string1[i], end=" ")
        print()

        # print column labels and matrix
        for i in range(len(matrix)):
            if i == 0:
                print("  ", end="")
            else:
                print(string0[i - 1], end=" ")
            for j in range(len(matrix[i])):
                print(matrix[i][j], end=" ")
            print()
        print()
    
    return matrix


def get_lcs(string0, string1, lcs_lengths_dp_matrix):
    '''
    returns the longest common subsequence of two strings according to the given matrix
    '''

    x = len(string0)
    y = len(string1)
    lcs = ""  # start with empty longest common subsequence

    while (x > 0) and (y > 0):

        # if current position in matrix is a match, 
        # then add the current position to longest common subsequence,
        # and move diagonally behind (one left one up)
        if string0[x - 1] == string1[y - 1]:
            lcs = string0[x - 1] + lcs  # add current character to front of LCS (can pick any of string0's or string1's character)
            x -= 1  # move left
            y -= 1  # move right

        # if current position is not a match then need to move up or left
        # decide up or left by seeing which cell has higher value in matrix
        else:

            # if cell on left has higher value than the one above, move left
            if lcs_lengths_dp_matrix[x - 1][y] > lcs_lengths_dp_matrix[x][y - 1]:
                x -= 1  

            # otherwise if cell above has higher value than the one on left, move up
            else:
                y -= 1

    return lcs


# run the program
if __name__ == "__main__":
    main()