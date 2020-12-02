n = int(input())

import math
temp = int(math.sqrt(n*2)) - 1

for i in range(temp, temp + 10):
    if i * (i+1) // 2 > (n+1):
        break

parted = (i-1)
print(n + 1 - parted)
