import math

n = int(input())
times = [int(input()) for _ in range(n)]

ans = times[0]
for t in times[1:]:
    ans = ans * t // math.gcd(ans, t)
print(ans)
