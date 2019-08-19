n = int(input())
nums =  list(map(int, input().split() ))

ans = 0
for i in range(n):
	ans += 1 / nums[i]
ans = 1 / ans
print(ans)
