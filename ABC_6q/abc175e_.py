# dp[r][c][p] := 位置r, cに到着し、該当行で拾ったアイテムがp個の時の、最大価値
# r = 0〜R, c = 0〜C, p = 0〜3

R, C, k = list(map(int, input().split()))
items = [list(map(int, input().split())) for _ in range(k)]

dp = [[[0 for _ in range(4)] for _ in range(C+1+1)] for _ in range(R+1+1)]  # 番兵

item_values = {}

for item in items:
    item_values[(item[0], item[1])] = item[2]

for r in range(1, R+1):
    for c in range(1, C+1):
        value_here = item_values.get((r, c), 0)

        if value_here == 0:
            dp[r][c][0] = max(
                dp[r][c-1][0],
                max(dp[r-1][c])
            )
            dp[r][c][1] = dp[r][c-1][1]
            dp[r][c][2] = dp[r][c-1][2]
            dp[r][c][3] = dp[r][c-1][3]
        
        else:
            dp[r][c][0] = max(
                dp[r][c-1][0],
                max(dp[r-1][c])
            )
            dp[r][c][1] = max([
                dp[r][c-1][1],
                dp[r][c-1][0] + value_here,
                max(dp[r-1][c]) + value_here
            ])

            dp[r][c][2] = max(dp[r][c-1][2], dp[r][c-1][1] + value_here)
            dp[r][c][3] = max(dp[r][c-1][3], dp[r][c-1][2] + value_here)
            
print(max(dp[R][C]))

# print(dp)
