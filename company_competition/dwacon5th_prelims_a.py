n = int(input())
nums = list(map(int, input().split()))

s = sum(nums)
min_dif = 10**10
for num in nums:
    dif = abs(s - num * n)
    min_dif = min(min_dif, dif)

for i, num in enumerate(nums):
    dif = abs(s - num * n)
    if min_dif == dif:
        print(i)
        exit()
