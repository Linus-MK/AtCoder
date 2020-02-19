# 公式解説に出ているのと同等のアルゴリズム
# 計算量は10*13*10^5 = 1300万

# ★WAが取り除けない！ ######

s = input()
# 下位から 1?2?3 だったら 0 → 3 → ?3 → 2?3 → …… の順にする 解説で最初に書いてたやつ

l = len(s)
dp = [[0 for _ in range(13)] for _ in range(l+1)]
mod = 10 ** 9 + 7

dp[-1][0] = 1
ten_power = 1
for digit in reversed(range(l)):
    if s[digit] != '?':
        for k in range(13):
            dp[digit][(k + int(s[digit]) * ten_power) % 13] += dp[digit+1][k]
    else:
        for k in range(13):
            for i in range(10):
                dp[digit][(k + i * ten_power) % 13] += dp[digit+1][k]
        for k in range(13):
            dp[digit][k] %= mod

    ten_power *= 10
    ten_power %= mod
        

print(dp[0][5] % mod)
