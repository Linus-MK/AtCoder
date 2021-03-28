n = int(input())

nums = list(map(int, input().split()))
nums.sort()

mod = 998244353
ans = 0
cumsum = 0
for i in range(n):
    ans += nums[i] * nums[i]
    ans %= mod

for i in reversed(range(n-1)):
    cumsum *= 2
    cumsum += nums[i+1]
    cumsum %= mod
    ans += nums[i] * cumsum
    ans %= mod
    
    # for j in range(i+1, n):
    #     ans += nums[i] * nums[j] * pow(2, j-i-1, mod)

print(ans % mod)
