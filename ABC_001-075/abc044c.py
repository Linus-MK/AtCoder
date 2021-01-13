# まぁ色々考えられるかー

# 平均がAという情報は割り算を含むので少々扱いづらい
# k個選んで合計がkA、と考え直す
# dp[i][j][s] := i枚目までの中からj枚選んで合計sになる選び方の数
# 答えは dp[n][k][kA] のkが1〜Nまでわたったときの和
# 計算量は[i]と[j]の最大がN, [s]の最大がx_i・Nなので、50*50*50*50 = 6250000が最大。
# でもPythonだとTLEだったわ

n, a = list(map(int, input().split()))
nums = list(map(int, input().split()))

dp = [[[0 for s in range(50*n+1)] for j in range(n+1)] for i in range(n+1)]

for i in range(n+1):
    dp[i][0][0] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        for s in range(50*n+1):
            if s-nums[i-1] >= 0:
                dp[i][j][s] = dp[i-1][j][s] + dp[i-1][j-1][s-nums[i-1]]
            else:
                dp[i][j][s] = dp[i-1][j][s]

ans = 0
for k in range(1, n+1):
    ans += dp[n][k][a*k]

print(ans)
