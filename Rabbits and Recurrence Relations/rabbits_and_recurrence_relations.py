memo = {1: 1, 2: 1}
def solution(n, k):

    # base case
    if n in memo:
        return memo[n]

    # no. of rabbits in last month plus no. of offsprings per pair multiplied by rabbits in last-to-last month
    memo[n] = solution(n - 1, k) + (k * solution(n - 2, k))
    return memo[n]


with open('rosalind_fib.txt', 'r') as f:
    n, k = f.readline().split()

n = int(n)
k = int(k)
ans = solution(n, k)
print(ans)