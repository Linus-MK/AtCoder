n, m = list(map(int, input().split()))

lis = [[] for i in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    lis[a-1].append(b)
    lis[b-1].append(a)

for i in range(n):
    length = len(lis[i])
    cities = sorted(lis[i])
    ans = list(map(str, [length] + cities))
    print(" ".join(ans))
