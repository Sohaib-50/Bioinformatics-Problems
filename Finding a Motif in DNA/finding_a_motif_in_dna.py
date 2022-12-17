def solution(s, t):
    ans = []
    current_search_start = 0
    current_search_start = s.find(t, current_search_start)
    while current_search_start != -1:
        current_search_start += 1
        ans.append(str(current_search_start))
        current_search_start = s.find(t, current_search_start)
    return ans



with open('rosalind_subs.txt', 'r') as f:
    s = f.readline().strip()
    t = f.readline().strip()

ans = solution(s, t)

print(" ".join(ans))