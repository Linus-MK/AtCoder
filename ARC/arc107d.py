# うまく加算すれば加算途中で1をまたぐことはないことに注意
# dp[i][s] := 要素数iで合計がsになる場合の数
# dp[i][s+1] = ?
# 実はこれ多重集合として同じやつでした　が厄介
### 同じやつでしたの重複分をあとで除算する → むずい。思いつかない。
### 同じやつでしたと言われない数え上げ方をする → 
# https://qiita.com/drken/items/f2ea4b58b0d21621bd51#6-%E5%88%86%E5%89%B2%E6%95%B0

# 1を含む→残りはdp[i-1][s-1]
# 1を含まない→全部1/2以下→2倍できる→dp[i][2s]

n, summ = list(map(int, input().split()))
mod = 998244353
 
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

dp[1][1] = 1
for i in range(2, n+1):
    for s in reversed(range(1, n+1)):
        if 2*s <= n:
            dp[i][s] = (dp[i-1][s-1] + dp[i][2*s]) % mod
        else:
            dp[i][s] = dp[i-1][s-1] % mod

# print(dp)
print(dp[n][summ])
