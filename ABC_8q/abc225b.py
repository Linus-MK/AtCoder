n = int(input())
d = dict()
for i in range(n-1):
    a, b = list(map(int, input().split()))
    d[a] = d.get(a, 0) + 1
    d[b] = d.get(b, 0) + 1

if max(d.values()) == n-1:
    print("Yes")
else:
    print("No")
