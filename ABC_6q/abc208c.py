n, sweets = list(map(int, input().split()))
nums = list(map(int, input().split()))

so = sorted(nums)
rest = sweets % n
th = so[rest]

for i in range(n):
    if nums[i] >= th:
        print(sweets//n)
    else:
        print(sweets//n + 1)