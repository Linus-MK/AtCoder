# フィボナッチ数列を一ひねりした問題に見えるのでDPだと思われるが、
# dp[idx]を求めるために和を取る要素の数が多くなりすぎるので、普通にやるとO(n^2)となりTLEする。
# 区間で区切られているところを見ると、dpの累積和を考えて、
# dp[p] 〜 dp[q]までの和をdp_cumsum[q] - dp_cumsum[p-1]と求めればよい。

n, k = list(map(int, input().split()))
period = [list(map(int, input().split())) for _ in range(k)]

dp = [0] * (2*n+1)
dp_cumsum = [0] * (2*n+1)
mod = 998244353

dp[n+1] = 1
dp_cumsum[n+1] = 1

for idx in range(n+2, 2*n+1):
    for l, r in period:
        # dp[idx - r] 〜dp[idx - l]までの和
        dp[idx] += dp_cumsum[idx - l] - dp_cumsum[idx - r - 1]

    dp[idx] %= mod
    dp_cumsum[idx] = (dp_cumsum[idx-1] + dp[idx]) % mod

print(dp[n+n])
# print(dp)
# print(dp_cumsum)

