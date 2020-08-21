k, t = list(map(int, input().split()))
nums = list(map(int, input().split()))

m = max(nums)
rest = k - m
if m - rest - 1 > 0:
    print(m - rest - 1)
else:
    print(0)
