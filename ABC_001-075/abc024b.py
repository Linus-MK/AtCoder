n, t = list(map(int, input().split()))

ans = 0
last = -10**10
for i in range(n):
    time = int(input())
    ans += min(time - last, t)
    last = time

print(ans)
