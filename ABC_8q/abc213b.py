n = int(input())
nums = list(map(int, input().split()))
boo = sorted(nums)[-2]
print(nums.index(boo) + 1)
