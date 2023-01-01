def longest_monotone_subsequence(sequence, increasing=True):
    dp = [[element] for element in sequence]  # for every element in sequence, stores longest monotone subsequence up untill that element's position

    for i in range(len(sequence)):
        
        for j in range(i):

            # if finding increasing and left element is smaller than right element OR finding decreasing and left element is larger than right element
            if ((sequence[j] < sequence[i]) and increasing) or ((sequence[j] > sequence[i]) and not increasing):

                # if longest subsequence until previous element is longer than current position's subsequence
                if len(dp[i]) <= len(dp[j]):
                    dp[i] = dp[j] + [sequence[i]]  # update current posiition's subsequence


    return sorted(dp, key=len)[-1]


def get_data(file_name):
    with open(file_name, 'r') as f:
        f.readline()
        permutation = f.readline().strip().split()
    return [int(x) for x in permutation]


permutation = get_data('rosalind_lgis.txt')

longest_increasing = longest_monotone_subsequence(permutation, increasing=True)
print(" " .join([str(x) for x in longest_increasing]))

longest_decreasing = longest_monotone_subsequence(permutation, increasing=False)
print(" " .join([str(x) for x in longest_decreasing]))

# write to file
with open('output.txt', 'w') as f:
    f.write(" " .join([str(x) for x in longest_increasing]) + "\n")
    f.write(" " .join([str(x) for x in longest_decreasing]))
    