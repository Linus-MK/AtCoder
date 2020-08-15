# dp[r][c][p] := 位置r, cに到着し、該当行で拾ったアイテムがp個の時の、最大価値
# r = 0〜R, c = 0〜C, p = 0〜3

R, C, k = list(map(int, input().split()))
items = [list(map(int, input().split())) for _ in range(k)]

dp = [[[0 for _ in range(4)] for _ in range(C+1+1)] for _ in range(R+1+1)]  # 番兵

item_values = [[0 for _ in range(C+1+1)] for _ in range(R+1+1)]

for item in items:
    item_values[item[0]][item[1]] = item[2]

for r in range(R+1):
    for c in range(C+1):
        value_r_plus = item_values[r+1][c]
        value_c_plus = item_values[r][c+1]
        now = dp[r][c]
        max_now = max(now)

        if value_r_plus > 0:
            # 上方にいどうしてアイテムを拾う
            dp[r+1][c][1] = max(dp[r+1][c][1], max_now + value_r_plus)
        
        # 上方に移動してアイテムを拾わない
        # dp[r+1][c][0] = max(dp[r+1][c][0], now[0], now[1], now[2], now[3])
        dp[r+1][c][0] = max(dp[r+1][c][0], max_now)

        # 右に移動してアイテムを拾わない
        dp[r][c+1][0] = max(dp[r][c+1][0], now[0])
        dp[r][c+1][1] = max(dp[r][c+1][1], now[1])
        dp[r][c+1][2] = max(dp[r][c+1][2], now[2])
        dp[r][c+1][3] = max(dp[r][c+1][3], now[3])

        if value_c_plus > 0:
            # 右に移動してアイテムを拾う
            dp[r][c+1][1] = max(dp[r][c+1][1], now[0] + value_c_plus)
            dp[r][c+1][2] = max(dp[r][c+1][2], now[1] + value_c_plus)
            dp[r][c+1][3] = max(dp[r][c+1][3], now[2] + value_c_plus)
            
print(max(dp[R][C]))

# print(dp)
