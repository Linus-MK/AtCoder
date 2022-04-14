n = int(input())

# x^2 - y = a^2
# (x+a)(x-a) = y <= N
# x-aで場合分け

import math
sq = int(math.sqrt(n))

ans = 0
for x_a in range(1, sq+1):
    upper = int(n // x_a)
    lower = x_a
    if upper >= lower:
        ans += int((upper - lower) //2) +1
    else:
        break

print(ans % 998244353)

