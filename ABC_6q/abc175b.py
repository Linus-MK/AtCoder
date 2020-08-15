n = int(input())
nums = list(map(int, input().split()))

nums.sort()

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if nums[i] != nums[j] and nums[j] != nums[k] and nums[k] < (nums[i]+nums[j]):
                ans += 1

print(ans)
