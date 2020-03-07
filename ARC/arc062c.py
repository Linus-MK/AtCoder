n = int(input())
vote_ratio = [ list(map(int, input().split())) for _ in range(n)]

# ans = vote_ratio[0] は同じオブジェクトを参照してしまうので避ける
ans = [vote_ratio[0][0], vote_ratio[0][1]]

for i in range(1,n):
	# bairitsu = max( math.ceil(ans[0] / vote_ratio[i][0]), math.ceil(ans[1] / vote_ratio[i][1]))
	# と書きたいところだが、浮動小数点数を経由したときに不正確になるので代わりにこうする。
	bairitsu = max( 
		(ans[0] + vote_ratio[i][0] - 1)// vote_ratio[i][0],
		(ans[1] + vote_ratio[i][1] - 1)// vote_ratio[i][1])
	ans = [vote_ratio[i][0] * bairitsu, vote_ratio[i][1] * bairitsu]

print(sum(ans))
