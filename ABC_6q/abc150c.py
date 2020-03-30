from itertools import permutations

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

for idx, perm in enumerate(permutations(range(1, n+1))):
    # perm は intからなるタプル
    res = True
    for ip in range(n):
        if p[ip] != perm[ip]:
            res = False
    if res:
        idx_p = idx
    res = True
    for iq in range(n):
        if q[iq] != perm[iq]:
            res = False
    if res:
        idx_q = idx

print(abs(idx_p - idx_q))
