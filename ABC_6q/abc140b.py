n = int(input())
a = list(map(int, input().split() ))
b = list(map(int, input().split() ))
c = list(map(int, input().split() ))

ans = 0
for k in range(n-1):
	if a[k+1] - a[k] == 1 :
		ans += c[a[k] - 1]

print(ans + sum(b))
