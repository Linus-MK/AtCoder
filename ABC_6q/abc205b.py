n = int(input())
nums = list(map(int, input().split()))

nums.sort()
ans = 'Yes'
for i in range(n):
    if nums[i] != i+1:
        ans = 'No'

print(ans)
