n = int(input())
ans = 0
for _ in range(n):
    a, b = list(map(int, input().split()))
    ans += min(a//2, b)
print(ans)