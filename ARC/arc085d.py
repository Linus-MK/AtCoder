n, x0, y0 = list(map(int, input().split()))

cards = [y0] + list(map(int, input().split()))
# yの手持ちはゲームに関与するため、リストに加えてしまう

xs = [[-1] * (n+1) for i in range(n+1)]
ys = [[-1] * (n+1) for i in range(n+1)] 
#xs[i][j] = xの手番で、xがcards[i]を持ちyがcards[j]を持っているとき(i<j)の最善スコア
#ys[i][j] = yの手番で、xがcards[j]を持ちyがcards[i]を持っているとき(i<j)の最善スコア

for i in range(n+1):
	xs[i][-1] = abs(cards[-1] - cards[i])
	ys[i][-1] = abs(cards[-1] - cards[i])

for j in range(n-1, -1, -1):

	# x[i][j] = max (y[j][j+1] , y[j][j+2] , ……, y[j][n] )
	xs_temp = max(ys[j][j+1:n+1])
	ys_temp = min(xs[j][j+1:n+1])
	for i in range(0, j):
		xs[i][j] = xs_temp
		ys[i][j] = ys_temp

# print(xs)
# print(ys)
print(max(ys[0][1:]))	
