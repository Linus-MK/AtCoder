h0, w0, h_end, w_end = list(map(int, input().split()))

dp = [[0 for _ in range(w_end+1)] for _ in range(h_end+1)]
mod = 998244353
dp[h0][w0] = 1

for h in range(h0, h_end + 1):
    for w in range(w0, w_end + 1):
        if (h, w) == (h0, w0):
            pass
        else:
            dp[h][w] = (dp[h][w-1] * h + dp[h-1][w] * w - dp[h-1][w-1] * (h-1) * (w-1)) % mod

print(dp[h_end][w_end])
