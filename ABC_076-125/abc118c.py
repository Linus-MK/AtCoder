import math

n = int(input())
nums = list(map(int, input().split()))

ans = nums[0]
for n in nums[1:]:
    ans = math.gcd(ans, n)
print(ans)
