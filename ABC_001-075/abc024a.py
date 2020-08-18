a, b, c, k = list(map(int, input().split()))
s, t = list(map(int, input().split()))

ans = s * a + t * b
if s+t >= k:
    ans -= (s+t) * c
print(ans)
