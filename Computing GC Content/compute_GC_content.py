def max_GC(sequences):
    max_ID = 0
    max_GC_content = 0
    for ID_ in sequences:
        current_GC_count = 0
        for char in sequences[ID_]:
            if char == 'G' or char == 'C':
                current_GC_count += 1

        current_GC_content = (current_GC_count / len(sequences[ID_])) * 100
        if current_GC_content > max_GC_content:
            max_GC_content = current_GC_content
            max_ID = ID_

    return max_ID, max_GC_content


with open('rosalind_gc.txt', 'r') as f:
    sequences = {}
    currrent_sequence = ""
    current_ID = 0
    for line in f:
        line = line.strip()
        if not line:
            continue

        if line[0] == ">":
            if currrent_sequence:
                sequences[current_ID] = currrent_sequence
                currrent_sequence = ""
            current_ID = line[1 : ]
        else:
            currrent_sequence += line

    sequences[current_ID] = currrent_sequence  

max_GC_ID, max_GC_content = max_GC(sequences)
print(max_GC_ID, max_GC_content, sep="\n")
