# pypy
a,b,c, n = list(map(int, input().split() ))

ans = 0
for i in range(3001):
	for j in range(3001):
		rest = n - a*i - b*j
		if rest >= 0 and rest % c == 0:
			ans += 1

print(ans)