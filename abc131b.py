n, start = list(map(int, input().split() ))

end = start + n - 1
sumall = (start + end ) * n // 2

ans = -(10**10)
for i in range(n):
	exclude = start + i
	if abs(exclude) < abs(ans - sumall):
		ans = sumall - exclude

print(ans)
