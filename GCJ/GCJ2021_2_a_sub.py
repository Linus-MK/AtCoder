import math
ans = 0
for i in range(2, 100+1):
    ans += math.ceil(10**8 / i)

print(ans / (10**8))

# 4.18737795 < 6 OK!
