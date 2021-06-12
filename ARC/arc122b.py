n = int(input())
nums = list(map(int, input().split()))
nums.sort()

mid = n//2
x = nums[mid] / 2

ans = x * n + sum(nums)
for i in range(n):
    ans -= min(nums[i], 2*x)
print(ans / n)
