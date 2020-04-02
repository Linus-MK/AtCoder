a, b = list(map(int, input().split()))

import fractions

print(a * b // fractions.gcd(a, b))
