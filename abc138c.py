n = int(input())
nums =  list(map(int, input().split() ))

nums.sort()

ans = nums[0]
for i in range(1, n):
	ans  = (ans + nums[i]) / 2
print(ans)
