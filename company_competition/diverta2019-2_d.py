# 個数制限なしナップサック問題を2回やる？

"""前半の交換：
重さはga, sa, ba 合計がN以下
価値がgb, sb, bb これを最大化
"""
n = int(input())
a_rate =list(map(int, input().split() ))
b_rate =list(map(int, input().split() ))
a_rate.append(1)
b_rate.append(1)

dp1 = [[0 for j in range(n+1)] for i in range(5)]

for i in range(4):
	for j in range(n+1):
		if j < a_rate[i]:
			dp1[i + 1][j] = dp1[i][j]
		else:
			dp1[i + 1][j] = max(dp1[i][j], dp1[i + 1][j - a_rate[i]] + b_rate[i])

mid_donguri = dp1[4][n]

dp2 = [[0 for j in range(mid_donguri+1)] for i in range(5)]

"""前半の交換：
重さはgb, sb, bb 合計がN以下
価値がga, sa, ba これを最大化
"""

for i in range(4):
	for j in range(mid_donguri+1):
		if j < b_rate[i]:
			dp2[i + 1][j] = dp2[i][j]
		else:
			dp2[i + 1][j] = max(dp2[i][j], dp2[i + 1][j - b_rate[i]] + a_rate[i])

print(dp2[4][mid_donguri])
