n, x = list(map(int, input().split()))
li = list(map(int, input().split()))

ans = 1
pos = 0
for i in range(n):
	pos = pos + li[i]
	if pos <= x:
		ans += 1
print(ans)