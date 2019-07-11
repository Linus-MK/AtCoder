# TODO: 添え字で大混乱してACまで1時間程度かかったので、適宜見直す必要あり

n, c = list(map(int, input().split()))

sushi = [list(map(int, input().split())) for _ in range(n)]

# 左のある箇所まで行ってから、右のある箇所まで行って終了
# 右のある箇所まで行ってから、左のある箇所まで行って終了
# のどっちか。「最初から右／左の一方向だけ行って終了」もあるが、上記2つの特殊パターンとして扱えることに解説を読んで気づいた。
value_sum = [0] * (n+1)
for i in range(n):
	value_sum[i+1] = value_sum[i] + sushi[i][1]
value_sum_inv = [0] * (n+1)
for i in range(n):
	value_sum_inv[i+1] = value_sum_inv[i] + sushi[n-1 - i][1]

max_arr = [0] * (n+1)
# max_arr = 始点からsushi[n]まで時計回りに進んでよい（その前に止まっても良い）ときの最適スコア
# [0, s[0]まで、s[1]まで、……]
for i in range(n):
	max_arr[i+1] = max(max_arr[i], value_sum[i+1] - sushi[i][0])

max_arr_inv = [0] * (n+1)
# max_arr_inv = 始点からsushi[n-1 - i]まで反時計回りに進んでよい（その前に止まっても良い）ときの最適スコア
# [0, s[n-1]まで、s[n-2]まで、……]
for i in range(n):
	max_arr_inv[i+1] = max(max_arr_inv[i], value_sum_inv[i+1] - (c - sushi[n-1 - i][0]) )

"""print(max_arr)
print(max_arr_inv)
"""
ans = 0 #移動なし

now = max_arr[n]
ans = max(ans, now)

for i in range(n-1, -1, -1): #最初に左に行くときの到達点
	now = value_sum_inv[n - i] - 2 * (c - sushi[i][0]) + max_arr[i]
	ans = max(ans, now)

now = max_arr_inv[n]
ans = max(ans, now)

for i in range(n): #最初に右に行くときの到達点
	now = value_sum[i+1] - 2 * (sushi[i][0]) + max_arr_inv[n-1 - i]
	ans = max(ans, now)
"""	print(now)
	print( value_sum[i+1] , (sushi[i][0]) , max_arr_inv[n-1 - i])
"""
print(ans)
