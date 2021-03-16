n = int(input())

inf = 10**10
ans = inf

for _ in range(n):
    a, price, stock = list(map(int, input().split()))
    if stock - a > 0 :
        ans = min(ans, price)

if ans == inf:
    print(-1)
else:
    print(ans)
