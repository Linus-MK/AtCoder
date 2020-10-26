n = int(input())
ans = -1
for _ in range(n):
    a, b = list(map(int, input().split()))
    ans = max(ans, a+b)
print(ans)
