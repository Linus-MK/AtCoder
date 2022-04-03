n = int(input())
nums = list(map(int, input().split()))

ans = nums[0]
for i in range(1, n):
    if nums[i-1] < nums[i]:
        ans = nums[i]
    else:
        break
print(ans)
