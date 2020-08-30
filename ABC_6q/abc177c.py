n = int(input())
nums = list(map(int, input().split()))

mod = 10**9 + 7

summm = sum(nums) % mod
sum_square = sum([num ** 2 for num in nums]) % mod

ans = (summm ** 2 - sum_square) % mod
ans *= (mod + 1) // 2
ans %= mod
print(ans)

