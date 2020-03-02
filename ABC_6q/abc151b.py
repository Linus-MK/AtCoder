n, k, m = list(map(int, input().split()))
nums = list(map(int, input().split()))

rest = m * n - sum(nums)
rest = max(0, rest)
if rest <= k:
    print(rest)
else:
    print(-1)
