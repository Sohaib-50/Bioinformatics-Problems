def permutations(n):
    permutations = []

    def dfs_permute(current_permutation, new, n):
        current_permutation += new

        if len(current_permutation) == n:
            permutations.append(current_permutation)
            return

        for i in range(1, n + 1):
            i = str(i)
            if i not in current_permutation:
                dfs_permute(current_permutation, i, n)


    for i in range(1, n + 1):
        i = str(i)
        dfs_permute("", i, n)

    return permutations


with open('rosalind_perm.txt', 'r') as f:
    n = int(f.readline().strip())

permutations = permutations(n)
print(len(permutations))
for permutation in permutations:
    print(" ".join(permutation))