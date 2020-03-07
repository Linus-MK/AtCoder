# 桁DPは、
# 「０以上N以下の整数で、ある条件を満たすものの個数を求めよ」
# 「０以上N以下の整数で、ある条件を満たすものの最大値を求めよ」
# といった問題を解く場合に用いられる方法です。
# https://qiita.com/pinokions009/items/1e98252718eeeeb5c9ab

n = input()
k_in = int(input())

# dp[i][smaller][k] := 上位からi桁目まで見て、smaller（nと一致しているいない）で非0の桁がk個だけあるものの数
# i <= 101, k <= 3 より、マス目の数は高々606。

# k = 4まで取っておくと（番兵）漸化式の場合分けをしなくて良いから楽。ただしループは
dp = [[[0 for _ in range(4 + 1)] for _ in range(2)] for _ in range(len(n))] 

digit = int(n[0])

dp[0][False][0] = 1
dp[0][False][1] = digit - 1
dp[0][True][1] = 1

for i in range(len(n) - 1):
    for smaller in [True, False]:
        for k in range(4):
            # 配るDPのほうが楽そうな予感
            if not smaller:
                # 0をつけたら
                dp[i+1][False][k] += dp[i][smaller][k]
                # 1~9をつけたら
                dp[i+1][False][k+1] += 9 * dp[i][smaller][k]
            else:
                next_digit = int(n[i+1])
                if next_digit == 0:
                    # 0をつけるしかない
                    dp[i+1][True][k] += dp[i][smaller][k]
                else:
                    # 0をつけたら
                    dp[i+1][False][k] += dp[i][smaller][k]
                    # 1〜(next_digit - 1)をつけたら
                    dp[i+1][False][k+1] += (next_digit - 1) * dp[i][smaller][k]
                    # next_digit をつけたら
                    dp[i+1][True][k+1] += dp[i][smaller][k]

print(dp[len(n)-1][True][k_in] + dp[len(n)-1][False][k_in])
