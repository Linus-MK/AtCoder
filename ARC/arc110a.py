# N=30と決めつけて良い
import math
ans = 1
for i in range(1, 30+1):
    gcd = math.gcd(ans, i)
    ans = ans * i // gcd
print(ans+1)
