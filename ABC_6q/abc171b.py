n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()

print(sum(nums[:k]))
