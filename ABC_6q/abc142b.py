n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
print(sum(map(lambda p: p>=k, nums)))
