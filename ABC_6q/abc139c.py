n = int(input())
nums = list(map(int, input().split()))

temp = 0
ans = 0

for i in range(n-1):
    if nums[i+1] <= nums[i]:
        temp += 1
    else:
        ans = max(temp, ans)
        temp = 0
ans = max(temp, ans)
print(ans)
