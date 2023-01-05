def P(n, k):
    ans = 1
    for i in range(n, n-k, -1):
        ans *= i
    return ans % 1000000


def get_data(file_name):
    with open(file_name, 'r') as f:
        n, k = f.readline().split()
        n, k = int(n), int(k)
    return n, k


data = get_data('rosalind_pper.txt')
ans = P(data[0], data[1])
print(ans)