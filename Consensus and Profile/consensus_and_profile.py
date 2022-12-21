def read_dna_strings(file_name):
    with open(file_name, 'r') as f:
        dna_strings = []
        current_dna_string = ""
        for line in f:
            if line[0] == ">":
                if current_dna_string:
                    dna_strings.append(current_dna_string)
                    current_dna_string = ""
            else:
                current_dna_string += line.strip()
    if current_dna_string:
        dna_strings.append(current_dna_string)
    return dna_strings


def get_profile_matrix(dna_strings):
    profile_matrix = {
        residue : [0 for _ in range(len(dna_strings[0]))] 
        for residue in "ACGT"
    }

    for dna in dna_strings:
        for position, residue in enumerate(dna):
            profile_matrix[residue][position] += 1
    
    return profile_matrix


def get_consensus_string(profile_matrix, length):
    consensus_string = ""

    # for every position in consensus string
    for position in range(length):

        # find out residue with most frequency at current position
        current_pos_max_residue = "A"
        for residue in "CGT":
            if profile_matrix[residue][position] > profile_matrix[current_pos_max_residue][position]:
                current_pos_max_residue = residue
        
        consensus_string += current_pos_max_residue

    return consensus_string


def main():
    dna_strings = read_dna_strings(file_name="rosalind_cons.txt")
    profile_matrix = get_profile_matrix(dna_strings)
    consensus_string = get_consensus_string(profile_matrix, len(dna_strings[0]))

    # write results to file, don't add newline to last line
    with open('output.txt', 'w') as f:
        f.write(consensus_string + "\n")
        for residue in "ACGT":
            f.write(f"{residue}: {' '.join([str(freq) for freq in profile_matrix[residue]])}")
            if residue != "T":
                f.write("\n")

if __name__ == "__main__":
    main()