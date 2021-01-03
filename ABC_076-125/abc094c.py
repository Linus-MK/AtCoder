n = int(input())

nums = list(map(int, input().split()))
sorted_nums = sorted(nums)

for i in range(n):
    if nums[i] <= sorted_nums[n//2 - 1]:
        print(sorted_nums[n//2])
    else:
        print(sorted_nums[n//2 - 1])
