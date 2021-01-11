# dp[i][t] := 料理がi種類目まで、制限時間t分のときの答え

# dp[i][t] = 
#   i種類目を使わない：dp[i-1][t]
#   i種類目を使う：dp[] あれ?注文はできないが食べるのはできるルールが難しいよ。

# brute-force型（料理の部分集合を全通り考える）だとどういう計算になる?
# 料理の集合がわかっていれば、食べる時間が最大のものを一番後回しにするのが最善（時間が最短で済む）
# 最大を除外した時間の和 <= 制限時間 - 1ならOK、そのうち満足度最大のものが答え
# （もちろん実際にやるとTLEになる）
# じゃあ食べる時間が小→大にソートしてから……いやそれでも、それまでの最後を食べるのに何分かかるかが分からないと無理だ。

# ------
# 2021年1月12日
# 解説AC

# 解説youtubeを文章に直す。なお解説PDFは2つ解法を載せている。この解法と、もう一つ別解法。
# まず、食べる料理の集合を固定したとき、 かかる時間は、Akの和 - 最後に食べたのにかかる時間An で求められる。
# ここでAkの和は食べる順序によらず一定なので、最後に食べるのはAiが最大となるiを選ぶのが最も良い。
# これより、Aに関してソートするのが良さそうだとわかる。
# Aの小から大の順に食べれば、「最後に食べるのはAiが最大となる」を満たせる。
# dp[i][time_limit] = 1個目〜i個目までの中からAの和がtime_limit以下になるように食べたときの、Bの和のmax

n, t = list(map(int, input().split()))
info = [list(map(int, input().split())) for i in range(n)]
# Aに関して昇順にソートする
info.sort(key=lambda x: x[0])

dp = [[0 for _ in range(t)] for _ in range(n)]

for i in range(n):
    for time_limit in range(t):
        if time_limit - info[i][0] >= 0:
            dp[i][time_limit] = max(dp[i-1][time_limit], dp[i-1][time_limit - info[i][0]] + info[i][1])
        else:
            dp[i][time_limit] = dp[i-1][time_limit]

# 最終的な答えは、
# 「1個目〜i個目までの中からAの和がt-1 以下になるように食べて、最後にi+1個目を食べる」の最大値
ans = 0
for i in range(n-1):
    ans = max(ans, dp[i][t-1] + info[i+1][1])

print(ans)
