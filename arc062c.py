# WA math.ceilは浮動小数点演算の影響を受けるので、正しく切り上げできないときがある
# >>> math.ceil((12345678901234*456+0.1)/12345678901234)
# 456
# >>> math.ceil((12345678901234*456+1)/12345678901234)
# 457

import math

n = int(input())
vote_ratio = [ list(map(int, input().split())) for _ in range(n)]
# print(vote_ratio)

# ans = vote_ratio[0] は同じオブジェクトを参照してしまうので避ける
ans = [vote_ratio[0][0], vote_ratio[0][1]]

for i in range(1,n):
	bairitsu = max(ans[0] / vote_ratio[i][0], ans[1] / vote_ratio[i][1])
	# bairitsu = math.ceil(bairitsu)
	bairitsu =  int(bairitsu)
	if vote_ratio[i][0] * bairitsu < ans[0] \
	or vote_ratio[i][1] * bairitsu < ans[1]:
		bairitsu += 1
	ans = [vote_ratio[i][0] * bairitsu, vote_ratio[i][1] * bairitsu]

print(sum(ans))
