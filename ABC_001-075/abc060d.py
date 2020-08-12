# 普通のナップサックは O(荷物の数、ナップサックに入る重量の上限)で計算できる。
# 今回はこれだと O(100 * 10**9) なので無理。
# 明らかに条件で重要なのは「すべてのi=2,3,...,Nについて、w_1<=w_i<=w_1+3」

# w_1が1000とする
# W = 4500→4つが必ず入り、5つは必ず入らない。価値の高いものから4つ。
# W = 4005→3つが必ず入る。4つが入るかどうかは場合による。
# max(3つの場合, 4つの場合)。3つは価値の高いものから3つ。4つは?
# 4つ選ぶ、4005以下、価値最大化
# dp[i][k][l]

# w_1〜w_iの中からk個選んで、重量をちょうどlにしたときの、最大価値
# dp[i][k][l] := max(dp[i-1][k][l], dp[i-1][k-1][l - w_i] + v_i)

# w_1〜w_iの中からk個選んで、重量をl以下にしたときの、最大価値
# dp[i][k][l] := max(dp[i-1][k][l], dp[i-1][k-1][l - w_i] + v_i)

# 後者を使うべき。更新式は同じで最後に重量に関してmaxを取る手間が無いので。
# i <= N, k <= N, l <= 3*N

n, w_limit = list(map(int, input().split()))

baggage = [list(map(int, input().split())) for _ in range(n)]

weight_base = baggage[0][0]

# i添字は0〜n-1 問題文から1引いて0-indexにする
# k添字は0〜n 
# l添字は0〜3n

for i in range(n):
    baggage[i][0] -= weight_base

dp = [[[0 for _ in range(3*n+1)] for _ in range(n+1)] for _ in range(n)]

for l in range(baggage[0][0], 3*n):
    dp[0][1][l] = baggage[0][1]

for i in range(1, n):
    for k in range(1, n+1):
        for l in range(3*n+1):
            if l - baggage[i][0] >= 0:
                dp[i][k][l] = max(dp[i-1][k][l], dp[i-1][k-1][l - baggage[i][0]] + baggage[i][1])
            else:
                dp[i][k][l] = dp[i-1][k][l]

valid_min_num = w_limit // (weight_base+3)
valid_max_num = w_limit // weight_base

ans = 0
for num in range(valid_min_num, min(valid_max_num, n) + 1):
    weight_rest = w_limit - weight_base * num
    if not 0 <= weight_rest:  # ここがないとREになるらしい。理由を要検討。
        continue
    elif weight_rest >= 3*n:
        weight_rest = 3*n

    # print(n-1, num, weight_rest)
    ans = max(ans, dp[n-1][num][weight_rest])

print(ans)
