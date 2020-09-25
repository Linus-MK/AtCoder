# 添字は多分コードとあってない
# dp[i][j] := sの最初i文字とtの最初j文字から作れる場合の数
# dp[i][j]の計算は
# Tのj文字目を使わない →dp[i][j-1]
# Tのj文字目を使う → S[a] = T[j] なる全てのaに対してdp[a-1][j-1]を計算して、その和。
# これをそのまま計算するとdpを1マス埋めるのにNかMだけかかってしまうので不可。
# 累積和のように「全ての和」を計算するのと、dpを計算するのを同時に実行する。

import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
s = list(map(int, input().split()))
t = list(map(int, input().split()))

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

# for x in dp[0]:
#     x = 1
dp[0] = [1 for _ in range(m+1)]
for y in dp:
    y[0] = 1

mod = 10**9 + 7

for j in range(1, m+1):
    char = t[j-1]
    cumsum = 0
    for i in range(1, n+1):
        if char == s[i-1]:
            cumsum += dp[i-1][j-1]
        dp[i][j] = (dp[i][j-1] + cumsum) % mod

print(dp[n][m])
