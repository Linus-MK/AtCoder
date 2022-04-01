n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

idx1 = 0
idx2 = 0

ans = 10**9 * 2
while idx1 < n and idx2 < m:
    ans = min(ans, abs(a[idx1] - b[idx2]))
    if a[idx1] > b[idx2]:
        idx2 += 1
    else:
        idx1 += 1
print(ans)
