import math
dim = int(input())
nums = list(map(int, input().split()))
print(sum(map(abs, nums)))
print(math.dist(nums, [0] * dim))
# print(math.sqrt(sum(map(lambda n: n**2, nums))))  # でも可
print(max(map(abs, nums)))
