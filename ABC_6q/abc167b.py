a, b, c, k = list(map(int, input().split()))

ans = 0
ans += 1 * min(k, a)

if a+b < k:
    ans += (-1) * (k-a-b)
print(ans)
