n = int(input())
a = list(map(int, input().split() ))

ans = a[0] + a[-1]
for k in range(n-2):
	ans += min(a[k], a[k+1])

print(ans)
