memo = {1: 1, 2: 1}
def solution(n, m):
    # base cases
    if n < 1:
        return 0
        
    elif n in memo:
        return memo[n]

    if n <= m:
        memo[n] = solution(n - 1, m) + solution(n - 2, m)
    elif n == m + 1:
        memo[n] = solution(n - 1, m) + solution(n - 2, m) - 1
    else:
        memo[n] = solution(n - 1, m) + solution(n - 2, m) - solution(n - m - 1, m)

    return memo[n]


with open('rosalind_fibd.txt', 'r') as f:
    n, m = f.readline().split()

n = int(n)
m = int(m)
ans = solution(n, m)
print(ans)