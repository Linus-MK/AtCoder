# ちゃんと証明せずに提出した。

n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    print(nums[0])
    exit()

import math

ans = nums[0]
for num in nums[1:]:
    ans = math.gcd(num, ans)

print(ans)
