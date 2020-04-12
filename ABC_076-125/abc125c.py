n = int(input())
nums = list(map(int, input().split()))

# maekara は 前から当該までの最大公約数
# ushirokara は 後ろから当該までの最大公約数
import fractions

maekara = [-1] * n
ushirokara = [-1] * n

maekara[0] = nums[0]
for i in range(1, n):
    maekara[i] = fractions.gcd(maekara[i-1], nums[i])

ushirokara[-1] = nums[-1]
for i in reversed(range(n-1)):
    ushirokara[i] = fractions.gcd(ushirokara[i+1], nums[i])

ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans, ushirokara[1])
    elif i == n-1:
        ans = max(ans, maekara[n-2])
    else:
        ans = max(ans, fractions.gcd(maekara[i-1], ushirokara[i+1]))
print(ans)
