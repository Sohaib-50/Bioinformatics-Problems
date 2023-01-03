def create_graph(dnas, K=3):
    adjacency_graph = []
    for fasta0 in dnas:
        for fasta1 in dnas:
            if fasta0 == fasta1:
                continue

            dna0 = dnas[fasta0]
            dna1 = dnas[fasta1]

            if dna0[len(dna0) - K : ] == dna1[ : K]:
                adjacency_graph.append((fasta0, fasta1))
    return adjacency_graph
        


def get_data(file_name):
    dnas = {}
    with open(file_name, 'r') as f:
        current_dna = ''
        current_fasta = f.readline().strip()[1:]
        for line in f:
            line = line.strip()
            if line[0] == '>':
                dnas[current_fasta] = current_dna
                current_dna = ''
                current_fasta = line[1:]
            else:
                current_dna += line
        dnas[current_fasta] = current_dna
    return dnas


data = get_data('rosalind_grph.txt')
graph = create_graph(data)

with open('output.txt', 'w') as f:
    for edge in graph:
        f.write(f"{edge[0]} {edge[1]}")
        f.write('\n')