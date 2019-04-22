import math

n, start = list(map(int, input().split()))
x = list(map(int, input().split()))

ans = abs(start - x[0])
for i in range(1, n):
	dist = abs(start - x[i])
	ans = math.gcd(ans, dist)
	# Python 3.5以上では正解になるはずだが、AtCoderでは3.4.3なのでmath.gcdが使えず、ランタイムエラーになる
print(ans)
