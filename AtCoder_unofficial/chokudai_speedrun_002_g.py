import math
n = int(input())
for _ in range(n):
    a, b = list(map(int, input().split()))
    print(math.gcd(a, b))
