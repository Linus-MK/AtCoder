n, s = list(map(int, input().split()))
nums = list(map(int, input().split()))

dp = [[0 for i in range(s+1)] for j in range(n+1)]
mod = 998244353

dp[0][0] = 1
for i in range(n):
    for summ in range(s+1):
        if summ - nums[i] >= 0:
            dp[i+1][summ] = (2 * dp[i][summ] + dp[i][summ - nums[i]]) % mod
        else:
            dp[i+1][summ] = (2 * dp[i][summ]) % mod


# print(dp)
print(dp[n][s] % mod)