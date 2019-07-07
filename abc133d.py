n = int(input())
dum = list(map(int, input().split()))

ans = [-1] * n

ans[0] = sum(dum[::2]) - sum(dum)//2

for i in range(1,n):
	ans[i] = dum[i-1] - ans[i-1]

for i in range(n):
	ans[i] *= 2
	ans[i] = str(ans[i])

print(" ".join(ans))
