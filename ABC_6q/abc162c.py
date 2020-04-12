import math

n = int(input())
ans = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        for k in range(j+1, n+1):
            ans += 6 * math.gcd(math.gcd(i, j), k)

for i in range(1, n+1):
    for j in range(i+1, n+1):
        ans += 6 * math.gcd(i, j)

for i in range(1, n+1):
        ans += i


print(ans)
