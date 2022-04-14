a, b = list(map(int, input().split()))
import math
length = math.sqrt(a**2 + b**2)
print(f"{a/length} {b/length}")
