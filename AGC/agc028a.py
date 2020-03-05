n, m = list(map(int, input().split()))
s = input()
t = input()

# import math
import fractions
gcdd = fractions.gcd(n, m)

for i in range(gcdd):
    if s[i*(n//gcdd)] != t[i*(m//gcdd)]:
        print(-1)
        exit()

print(n*m//gcdd)
