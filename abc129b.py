num = int(input())
arr = list(map(int, input().split() ))

ans = 10**10
for i in range(num):
	left_sum = sum(arr[:i])
	right_sum = sum(arr[i:])
	ans = min(ans, abs(left_sum - right_sum))
print(ans)
