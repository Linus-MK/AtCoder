n = int(input())
heights = list(map(int, input().split() ))

ans = "Yes"
for i in range(1, n):
	if heights[i] > heights[i-1]:
		heights[i] -= 1
	if heights[i] < heights[i-1]:
		ans = "No"
		break

print(ans)