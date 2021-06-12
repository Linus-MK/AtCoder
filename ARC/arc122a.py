n = int(input())
nums = list(map(int, input().split()))

# dp[i][0] i番目まで、最後が-、の和
# dp[i][1] i番目まで、最後が+、の和
if n == 1:
    print(nums[0])
    exit()

dp = [[0 for i in range(2)] for j in range(n)]
kosu = [[0 for i in range(2)] for j in range(n)]

dp[1][0] = nums[0] - nums[1]
dp[1][1] = nums[0] + nums[1]
kosu[1][0] = 1
kosu[1][1] = 1

mod = 10**9 + 7
for i in range(2, n):
    dp[i][0] = dp[i-1][1] - kosu[i-1][1] * nums[i]
    dp[i][1] = dp[i-1][1] + kosu[i-1][1] * nums[i] + dp[i-1][0] + kosu[i-1][0] * nums[i]
    kosu[i][0] = kosu[i-1][1]
    kosu[i][1] = kosu[i-1][1] + kosu[i-1][0]

    dp[i][0] %= mod
    dp[i][1] %= mod
    kosu[i][0] %= mod
    kosu[i][1] %= mod


print((dp[n-1][0] + dp[n-1][1]) % mod)
# print(kosu[n-1][0] + kosu[n-1][1])
# print(kosu)
# print(dp)
